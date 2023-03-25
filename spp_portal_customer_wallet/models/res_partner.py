# SPDX-FileCopyrightText: 2023 Coop IT Easy SC
#
# SPDX-License-Identifier: AGPL-3.0-or-later

from collections import defaultdict

from odoo import models


class ResPartner(models.Model):
    _inherit = "res.partner"

    def customer_wallet_payments_per_month(self):
        """Return a dictionary with (year, month) keys. The value is the amount
        spent using the customer wallet for every month.
        """
        self.ensure_one()
        # Like in account_customer_wallet, search against all partners in family.
        all_partners_in_family = self.get_all_partners_in_family()
        all_account_ids = (
            self.env["res.partner"]
            .browse(all_partners_in_family)
            .mapped("customer_wallet_account_id")
        )
        move_lines = self.env["account.move.line"].search(
            [
                ("partner_id", "in", all_partners_in_family),
                ("account_id", "in", all_account_ids.ids),
                # Negative balances = fill up the customer wallet. We're only
                # interested in customer wallet spendings here, so let's skip
                # them.
                ("balance", ">", 0),
            ]
        )
        per_month_dict = defaultdict(int)
        for move_line in move_lines:
            date = move_line.move_id.date
            per_month_dict[(date.year, date.month)] += move_line.balance
        # Don't return defaultdict
        return per_month_dict

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
