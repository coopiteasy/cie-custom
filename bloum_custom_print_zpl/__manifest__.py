# SPDX-FileCopyrightText: 2026 Coop IT Easy SC
#
# SPDX-License-Identifier: AGPL-3.0-or-later

{
    "name": "Bloum Custom Print ZPL",
    "summary": (
        "Filter ZPL commands to remove instructions unsupported by Bloum's "
        "Zebra SD220 printer"
    ),
    "version": "16.0.1.0.0",
    "category": "Uncategorized",
    "website": "https://coopiteasy.be",
    "author": "Coop IT Easy SC",
    "license": "AGPL-3",
    "depends": [
        "pos_self_service_weighing_print_zpl",
    ],
    "assets": {
        "point_of_sale.assets": [
            "bloum_custom_print_zpl/static/src/js/**/*.js",
        ],
    },
}
