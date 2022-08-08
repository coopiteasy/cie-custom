# SPDX-FileCopyrightText: 2022 Coop IT Easy SC
#
# SPDX-License-Identifier: AGPL-3.0-or-later

from odoo import models


class PaymentTransaction(models.Model):
    _inherit = "payment.transaction"

    def _link_down_payment_to_orders(self):
        """
        When a transaction is set to done, link the account.payment and its
        account.move.lines to the sale order as down payments.
        """
        for transaction in self:
            for order in transaction.sale_order_ids:
                transaction.payment_id.sale_id = order
                for line in transaction.payment_id.move_line_ids:
                    if line.account_id.internal_type == "receivable":
                        line.sale_id = order

    def _post_process_after_done(self):
        res = super()._post_process_after_done()
        self._link_down_payment_to_orders()
        return res
