# Copyright 2023 Akretion
# @author Olivier Nibart <olivier.nibart@akretion.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from freezegun import freeze_time

from odoo import fields
from odoo.tests.common import Form

from .common import UgessMembershipCommon


class TestWizardMembershipInvoice(UgessMembershipCommon):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        # cls.membership_id is of type custom, cf. inheritance

        cls.membership_template_id_fixed = cls.env["product.template"].create(
            {
                "name": "Test Membership",
                "membership_type": "fixed",
                "membership": True,
                "membership_date_from": fields.Date.to_date("2023-01-01"),
                "membership_date_to": fields.Date.to_date("2023-08-31"),
            }
        )
        cls.membership_id_fixed = cls.membership_template_id_fixed.product_variant_id

        cls.membership_template_id_variable = cls.env["product.template"].create(
            {
                "name": "Test Membership",
                "membership_type": "variable",
                "membership": True,
                "membership_interval_qty": 2,
                "membership_interval_unit": "months",
            }
        )
        cls.membership_id_variable = (
            cls.membership_template_id_variable.product_variant_id
        )

        cls.wizard_membership_invoice = cls.env["membership.invoice"].create(
            {
                "product_id": cls.membership_id.id,
                "member_price": 1.0,
            }
        )

    def test_get_current_membership_dates_custom(self):
        membership_id = self.membership_id
        self.assertEqual(membership_id.membership_type, "custom")
        (
            date_from,
            date_to,
        ) = self.wizard_membership_invoice._get_current_membership_dates(membership_id)
        self.assertFalse(date_from)
        self.assertFalse(date_to)
        self.assertFalse(self.wizard_membership_invoice.current_membership_date_from)
        self.assertFalse(self.wizard_membership_invoice.current_membership_date_to)

    def test_get_current_membership_dates_fixed(self):
        membership_id = self.membership_id_fixed
        self.assertEqual(membership_id.membership_type, "fixed")
        (
            date_from,
            date_to,
        ) = self.wizard_membership_invoice._get_current_membership_dates(membership_id)
        self.assertEqual(date_from, fields.Date.to_date("2023-01-01"))
        self.assertEqual(date_to, fields.Date.to_date("2023-08-31"))
        self.assertEqual(
            self.wizard_membership_invoice.current_membership_date_from,
            fields.Date.to_date("2023-01-01"),
        )
        self.assertEqual(
            self.wizard_membership_invoice.current_membership_date_to,
            fields.Date.to_date("2023-08-31"),
        )

    @freeze_time("2023-09-01")
    def test_get_current_membership_dates_variable(self):
        membership_id = self.membership_id_variable
        self.assertEqual(membership_id.membership_type, "variable")
        (
            date_from,
            date_to,
        ) = self.wizard_membership_invoice._get_current_membership_dates(membership_id)
        params = self.env["account.move.line"]._prepare_membership_line(
            self.env["account.move"].browse(),
            membership_id,
            None,
            None,
        )
        self.assertEqual(date_from, params["date_from"])
        self.assertEqual(date_to, params["date_to"])
        self.assertEqual(
            self.wizard_membership_invoice.current_membership_date_from,
            params["date_from"],
        )
        self.assertEqual(
            self.wizard_membership_invoice.current_membership_date_to, params["date_to"]
        )

    def test_onchange_product(self):
        wizard = self.wizard_membership_invoice
        self.assertEqual(wizard.product_id, self.membership_id)
        wizard.onchange_product()
        self.assertFalse(wizard.date_from)
        self.assertFalse(wizard.date_to)
        wizard.product_id = self.membership_id_fixed
        wizard.onchange_product()
        self.assertEqual(wizard.date_from, fields.Date.to_date("2023-01-01"))
        self.assertEqual(wizard.date_to, fields.Date.to_date("2023-08-31"))

    def test_do_invoice(self):
        partner = self.env["res.partner"].create({"name": "Test Invoice partner"})
        invoice_form = Form(
            self.env["membership.invoice"].with_context(default_partner_id=partner.id)
        )
        invoice_form.product_id = self.membership_id
        invoice_form.date_from = "2023-01-01"
        invoice_form.date_to = "2023-12-31"
        invoice_form.expenditure_ceiling = 100
        invoice_form.expenditure_ceiling_period = "month"
        with invoice_form.expenditure_override_ids.new() as override:
            override.date_from = "2023-02-01"
            override.date_to = "2023-02-28"
            override.expenditure_ceiling = 50
        invoice = invoice_form.save()

        res = invoice.with_context(
            active_ids=invoice.partner_id.ids
        ).membership_invoice()
        account_moves = self.env["account.move"].search(res["domain"])
        membership_line = account_moves.mapped("invoice_line_ids.membership_lines")

        self.assertEqual(len(membership_line), 1)
        self.assertEqual(membership_line.date_from.isoformat(), "2023-01-01")
        self.assertEqual(membership_line.date_to.isoformat(), "2023-12-31")
        self.assertEqual(membership_line.expenditure_ceiling, 100)
        self.assertEqual(membership_line.expenditure_ceiling_period, "month")

        self.assertEqual(len(membership_line.expenditure_override_ids), 1)
        self.assertEqual(
            membership_line.expenditure_override_ids.date_from.isoformat(), "2023-02-01"
        )
        self.assertEqual(
            membership_line.expenditure_override_ids.date_to.isoformat(), "2023-02-28"
        )
        self.assertEqual(
            membership_line.expenditure_override_ids.expenditure_ceiling, 50
        )
