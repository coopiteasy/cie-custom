# SPDX-FileCopyrightText: 2022 Coop IT Easy SC
#
# SPDX-License-Identifier: AGPL-3.0-or-later

from odoo import models


class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    def action_invoice_paid(self):
        """When an invoice is paid, link the account.payment and its
        account.move.lines to the sale order as down payments.
        """
        to_pay_invoices = self.filtered(lambda inv: inv.state != "paid")
        super().action_invoice_paid()

        for invoice in to_pay_invoices:
            sale_order_id = self.env["sale.order"].search(
                [("name", "=", invoice.origin)]
            )
            if not sale_order_id:
                continue
            for payment_id in invoice.payment_ids:
                payment_id.sale_id = sale_order_id
            for line in invoice.payment_move_line_ids:
                if line.account_id.internal_type == "receivable":
                    line.sale_id = sale_order_id
