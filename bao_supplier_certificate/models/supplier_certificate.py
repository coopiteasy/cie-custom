# SPDX-FileCopyrightText: 2023 Coop IT Easy SC
#
# SPDX-License-Identifier: AGPL-3.0-or-later

from odoo import _, api, fields, models
from odoo.exceptions import UserError


class SupplierCertificate(models.Model):

    _name = "bao.supplier.certificate"
    _description = "Supplier Certificate"

    name = fields.Char()
    supplier_certificate_generator_id = fields.Many2one(
        string="Generator",
        comodel_name="bao.supplier.certificate.generator",
        ondelete="cascade",
    )
    partner_id = fields.Many2one(
        comodel_name="res.partner",
        required=True,
    )
    start_date = fields.Date(required=True)
    end_date = fields.Date(required=True)
    state = fields.Selection(
        selection=[
            ("draft", _("Draft")),
            ("confirmed", _("Confirmed")),
            ("sent", _("Sent")),
            ("cancelled", _("Cancelled")),
        ],
        default="draft",
    )
    purchase_order_ids = fields.Many2many(
        comodel_name="purchase.order",
        compute="_compute_purchase_order_ids",
    )

    @api.depends("partner_id", "start_date", "end_date")
    def _compute_purchase_order_ids(self):
        """Compute purchase order that belong to supplier_id between
        date_from and date_to.
        """
        for certificate in self:
            certificate.purchase_order_ids = self.env["purchase.order"].search(
                [
                    ("state", "in", ["purchase", "done"]),
                    ("partner_id", "=", certificate.partner_id.id),
                    ("date_approve", ">=", certificate.start_date),
                    ("date_approve", "<=", certificate.end_date),
                ]
            )

    def action_confirm(self):
        """Confirm Certificate"""
        for certificate in self:
            certificate.state = "confirmed"

    def action_cancel(self):
        """Cancel Certificate"""
        for certificate in self:
            if certificate.state != "sent":
                certificate.state = "cancelled"
            else:
                raise UserError(
                    _("Cannot cancel a certificate that has been already sent.")
                )

    def action_send_email(self):
        """Send certificate by email"""
        for certificate in self:
            if certificate.state in ("confirmed", "sent"):
                mail_template = self.env.ref(
                    "bao_supplier_certificate.email_template_supplier_certificate"
                )
                mail_template.send_mail(certificate.id)
                certificate.state = "sent"
        return {"toast_message": _("Vendor Certificate has been sent.")}
