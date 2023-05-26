# SPDX-FileCopyrightText: 2023 Coop IT Easy SC
#
# SPDX-License-Identifier: AGPL-3.0-or-later

from collections import defaultdict

from odoo import models


class ResPartner(models.Model):
    _inherit = "res.partner"

    def foodprint_payments_per_month(self):
        """Very specifically: the sum of foodprint payments each month made in
        the POS using (at least partially) the customer wallet payment method.
        Return a dictionary with (year, month) keys and the corresponding value.
        """
        self.ensure_one()
        order_lines = self.env["pos.order.line"].search(
            [
                ("order_id.partner_id", "=", self.id),
                ("product_id.is_foodprint_label", "=", True),
            ]
        )
        wallet_account = self.customer_wallet_account_id
        per_month_dict = defaultdict(int)
        for line in order_lines:
            # Filter out pos orders that were not made using the customer
            # wallet. TODO: Can we do this using a domain instead of a for-loop?
            order = line.order_id
            statement_lines = order.statement_ids
            for statement_line in statement_lines:
                if statement_line.statement_id.account_id == wallet_account:
                    break
            else:
                continue

            date = order.date_order
            per_month_dict[(date.year, date.month)] += line.price_subtotal_incl
        return per_month_dict
