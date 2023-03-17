# SPDX-FileCopyrightText: 2023 Coop IT Easy SC
#
# SPDX-License-Identifier: AGPL-3.0-or-later

from collections import defaultdict

from odoo.http import request
from odoo.tools.translate import _

from odoo.addons.portal.controllers.portal import CustomerPortal


def translate_month(number):
    MONTHS = {
        1: _("January"),
        2: _("February"),
        3: _("March"),
        4: _("April"),
        5: _("May"),
        6: _("June"),
        7: _("July"),
        8: _("August"),
        9: _("September"),
        10: _("October"),
        11: _("November"),
        12: _("December"),
    }
    return MONTHS[number]


def sums_of_years(per_month):
    result = defaultdict(int)
    for key, value in per_month.items():
        result[key[0]] += value
    return dict(result)


class PortalPosOrderAmount(CustomerPortal):
    def _prepare_portal_layout_values(self):
        values = super(PortalPosOrderAmount, self)._prepare_portal_layout_values()
        user = request.env.user
        partner_id = user.partner_id

        per_month = partner_id.customer_wallet_payments_per_month()
        per_year = sums_of_years(per_month)
        foodprint_per_month = partner_id.foodprint_payments_per_month()
        foodprint_per_year = sums_of_years(foodprint_per_month)

        ordered = []
        years = set()
        for key, value in sorted(per_month.items(), reverse=True):
            year = key[0]
            month = key[1]
            if year not in years:
                ordered.append(
                    {
                        "month": str(year),
                        "amount": per_year[year],
                        "foodprint_amount": foodprint_per_year.get(year, 0),
                    }
                )
                years.add(year)
            ordered.append(
                {
                    "month": f"{translate_month(month)} {year}",
                    "amount": value,
                    "foodprint_amount": foodprint_per_month.get(key, 0),
                }
            )

        values["customer_wallet_payments_per_month"] = ordered
        values["company_currency"] = (
            request.env["res.company"]._company_default_get().currency_id
        )
        values["customer_wallet_balance"] = partner_id.customer_wallet_balance
        return values
