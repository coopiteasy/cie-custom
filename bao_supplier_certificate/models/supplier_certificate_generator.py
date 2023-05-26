# SPDX-FileCopyrightText: 2023 Coop IT Easy SC
#
# SPDX-License-Identifier: AGPL-3.0-or-later

from odoo import _, api, fields, models
from odoo.exceptions import UserError


class SupplierCertificateGenerator(models.Model):

    _name = "bao.supplier.certificate.generator"
    _description = "Supplier Certificate Generator"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    name = fields.Char()
    start_date = fields.Date(required=True)
    end_date = fields.Date(required=True)
    state = fields.Selection(
        selection=[
            ("draft", _("Draft")),
            ("confirmed", _("Confirmed")),
            ("cancelled", _("Cancelled")),
        ],
        default="draft",
    )
    sent = fields.Boolean(
        compute="_compute_sent",
        help="Are all certificates sent?",
    )
    supplier_ids = fields.Many2many(
        string="Vendors",
        comodel_name="res.partner",
        help="Leave this field empty to automatically select Vendors "
        "that have a Purchase Order confirmed between Start Date and "
        "End Date.",
    )
    supplier_certificate_ids = fields.One2many(
        string="Certificates",
        comodel_name="bao.supplier.certificate",
        inverse_name="supplier_certificate_generator_id",
    )
    supplier_certificate_count = fields.Integer(
        compute="_compute_supplier_certificate_count",
        string="Certificate Count",
        copy=False,
        default=0,
        store=True,
    )

    @api.depends("supplier_certificate_ids")
    def _compute_supplier_certificate_count(self):
        """Compute the number of supplier_certificate_ids"""
        for certificate_generator in self:
            certificate_generator.supplier_certificate_count = len(
                certificate_generator.supplier_certificate_ids
            )

    @api.depends("supplier_certificate_ids")
    def _compute_sent(self):
        """Compute the number of supplier_certificate_ids"""
        for certificate_generator in self:
            sent_certificates = certificate_generator.supplier_certificate_ids.filtered(
                lambda r: r.state == "sent"
            )
            certificate_generator.sent = len(sent_certificates) == len(
                certificate_generator.supplier_certificate_ids
            )

    def _get_related_supplier_certificate_domain(self):
        """Return domain used to show related bao.supplier.certificate."""
        return [("supplier_certificate_generator_id", "=", self.id)]

    def action_supplier_certificate(self):
        """This function returns an action that display existing
        Supplier Certificate of the current Supplier Certificate
        Generator.
        """
        action = self.env["ir.actions.act_window"]._for_xml_id(
            "bao_supplier_certificate.action_supplier_certificate"
        )
        action["domain"] = self._get_related_supplier_certificate_domain()
        return action

    def action_confirm(self):
        """Confirme Certificate Generator and generate Certificates"""
        for generator in self:
            # Fill in supplier_ids if empty
            if not generator.supplier_ids:
                generator.supplier_ids = generator.get_supplier_ids()
            val_list = []
            for supplier in generator.supplier_ids:
                val_list.append(
                    {
                        "name": "{} - {}".format(generator.name, supplier.name),
                        "state": "confirmed",
                        "supplier_certificate_generator_id": generator.id,
                        "partner_id": supplier.id,
                        "start_date": generator.start_date,
                        "end_date": generator.end_date,
                    }
                )
            self.env["bao.supplier.certificate"].create(val_list)
            generator.state = "confirmed"

    def action_send_email(self):
        """Send email for all related Certificates"""
        for generator in self:
            generator.supplier_certificate_ids.action_send_email()

    def action_cancel(self):
        """Cancel Certificate Generator and cancel all related Certificates"""
        state = self.mapped("state")
        if "sent" in state:
            raise UserError(
                _("Cannot cancel a certificate that has been already sent.")
            )
        for generator in self:
            generator.supplier_certificate_ids.action_cancel()
            generator.state = "cancelled"

    def get_supplier_ids(self):
        """Return supplier that have at least one purchase order that
        will be certified by this generator.
        """
        self.ensure_one()
        purchase_order_ids = self.env["purchase.order"].search(
            [
                ("state", "in", ["purchase", "done"]),
                ("date_approve", ">=", self.start_date),
                ("date_approve", "<=", self.end_date),
            ]
        )
        # mapped() removes duplicates partner_id
        return purchase_order_ids.mapped("partner_id")
