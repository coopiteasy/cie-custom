# Copyright 2020 Coop IT Easy SCRL fs
#   Robin Keunen <robin@coopiteasy.be>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import api, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    @api.multi
    def action_invoice_create(self, grouped=False, final=False):
        invoice_ids = super().action_invoice_create(grouped=grouped, final=final)
        invoices = self.env["account.invoice"].browse(invoice_ids)
        immediate_payment_term_id = self.env.ref(
            "account.account_payment_term_immediate"
        )
        invoices.payment_term_id = immediate_payment_term_id
        invoices.action_invoice_open()
        return invoice_ids
