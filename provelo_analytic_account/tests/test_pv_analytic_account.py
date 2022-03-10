# Copyright 2021 Coop IT Easy SCRL fs
#   Robin Keunen <robin@coopiteasy.be>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).


from datetime import datetime, timedelta

from odoo.addons.resource_activity.tests.test_base import TestResourceActivityBase


class TestProVeloBobCodes(TestResourceActivityBase):
    def setUp(self):
        super().setUp()
        self.account_account = self.env["account.account"].create(
            {
                "name": "test account",
                "code": "TACC",
                "user_type_id": self.ref("account.data_account_type_revenue"),
                "tag_ids": [(6, 0, [self.ref("account.account_tag_operating")])],
            }
        )
        self.journal = self.env["account.journal"].create(
            {
                "name": "test journal",
                "code": "TINV",
                "type": "sale",
                "default_credit_account_id": self.account_account.id,
                "default_debit_account_id": self.account_account.id,
                "refund_sequence": True,
            }
        )
        self.main_location.write(
            {
                "bob_code": "MAINLOC",
                "journal_id": self.journal.id,
            }
        )
        self.hr_department = self.env["hr.department"].create(
            {
                "name": "test department",
                "bob_code": "TDEP",
            }
        )
        self.allowed_financing = self.env["pv.financing"].create(
            {"name": "allowed financing", "bob_code": "AFIN"}
        )
        self.not_allowed_financing = self.env["pv.financing"].create(
            {"name": "not allowed financing", "bob_code": "NAFIN"}
        )
        self.project = self.env["pv.project"].create(
            {
                "name": "test project",
                "bob_code": "TPRO",
                "location_id": self.main_location.id,
                "department_id": self.hr_department.id,
                "allowed_financing_ids": [(6, None, [self.allowed_financing.id])],
            }
        )
        self.activity_type.project_id = self.project

    def test_assign_account_invoice_analytic_account(self):
        date_start = datetime.now()
        date_end = date_start + timedelta(hours=2)

        registration = {
            "attendee_id": self.partner_demo.id,
            "quantity": 2,
            "quantity_needed": 2,
            "booking_type": "booked",
            "resource_category": self.mtb_category.id,
            "product_id": self.bike_product.id,
        }

        activity = self.env["resource.activity"].create(
            {
                "location_id": self.main_location.id,
                "activity_type": self.activity_type.id,
                "date_start": date_start,
                "date_end": date_end,
                "resource_allocation_start": date_start,
                "resource_allocation_end": date_end,
                "registrations": [(0, 0, registration)],
            }
        )
        activity.search_all_resources()
        activity.reserve_needed_resource()

        activity.create_sale_order()
        activity.action_sale_order()
        sale_order = activity.sale_orders
        invoice_id = sale_order.action_invoice_create()
        invoice = self.env["account.invoice"].browse(invoice_id)
        self.assertEquals(invoice.activity_id, activity)
        self.assertEquals(invoice.project_id, self.project)
        self.assertEquals(invoice.location_id, self.main_location)
        self.assertEquals(invoice.department_id, self.hr_department)
        self.assertEquals(invoice.allowed_financing_ids, self.allowed_financing)
        self.assertEquals(invoice.journal_id, self.journal)
