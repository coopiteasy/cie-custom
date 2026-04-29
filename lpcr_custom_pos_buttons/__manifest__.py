# SPDX-FileCopyrightText: 2026 Coop IT Easy SC
#
# SPDX-License-Identifier: AGPL-3.0-or-later

{
    "name": "LPCR Custom PoS Buttons",
    "summary": "Add a button redirecting to the lpcr contact form and another to the "
    "members national view in the PoS",
    "version": "16.0.1.0.0",
    "category": "Sales/Point of Sale",
    "website": "https://coopiteasy.be",
    "author": "Coop IT Easy SC",
    "maintainers": ["mihien"],
    "license": "AGPL-3",
    "depends": [
        "point_of_sale",
        "membership_global_member_view",
        "lpcr_website_partner_form",
    ],
    "assets": {
        "point_of_sale.assets": [
            "lpcr_custom_pos_buttons/static/src/**/*.js",
            "lpcr_custom_pos_buttons/static/src/**/*.scss",
            "lpcr_custom_pos_buttons/static/src/**/*.xml",
        ],
    },
}
