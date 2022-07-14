# SPDX-FileCopyrightText: 2022 Coop IT Easy SC
#
# SPDX-License-Identifier: AGPL-3.0-or-later

from odoo import models


class PaymentTransaction(models.Model):
    _inherit = "payment.transaction"

    def _post_process_after_done(self):
        """When a transaction is set to done, link the account.payment and its
        account.move.lines to the sale order as down payments.
        """
        res = super()._post_process_after_done()
        for order in self.sale_order_ids:
            self.payment_id.sale_id = order
            for line in self.payment_id.move_line_ids:
                if line.account_id.internal_type == "receivable":
                    line.sale_id = order
        return res
