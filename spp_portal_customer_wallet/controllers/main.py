# SPDX-FileCopyrightText: 2023 Coop IT Easy SC
#
# SPDX-License-Identifier: AGPL-3.0-or-later

from odoo.http import request

from odoo.addons.portal_customer_wallet.controllers.main import (
    CustomerWalletAmountPortal,
    sums_of_years,
)


class FoodprintAmountPortal(CustomerWalletAmountPortal):
    def _prepare_portal_layout_values(self):
        values = super(FoodprintAmountPortal, self)._prepare_portal_layout_values()
        user = request.env.user
        partner_id = user.partner_id

        foodprint_per_month = partner_id.foodprint_payments_per_month()
        foodprint_per_year = sums_of_years(foodprint_per_month)

        ordered = values["customer_wallet_payments_per_month"]

        for item in ordered:
            year = item["year_month"][0]
            month = item["year_month"][1]
            if not month:
                item["foodprint_amount"] = foodprint_per_year.get(year, 0)
            else:
                item["foodprint_amount"] = foodprint_per_month.get((year, month), 0)

        return values
