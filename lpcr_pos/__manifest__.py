# SPDX-FileCopyrightText: 2025 Coop IT Easy SC
#
# SPDX-License-Identifier: AGPL-3.0-or-later

{
    "name": "PoS Customizations for LPCR",
    "summary": "Customize the PoS according to LPCR specifications",
    "version": "16.0.1.0.0",
    "category": "Sales/Point of Sale",
    "website": "https://coopiteasy.be",
    "author": "Coop IT Easy SC",
    "license": "AGPL-3",
    "depends": [
        "pos_hide_partner_info",
        "pos_sale",
    ],
    "assets": {
        "point_of_sale.assets": [
            "lpcr_pos/static/src/js/**/*.js",
            "lpcr_pos/static/src/xml/**/*.xml",
        ],
    },
}
