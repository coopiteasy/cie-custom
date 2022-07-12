# SPDX-FileCopyrightText: 2022 Coop IT Easy SC
#
# SPDX-License-Identifier: AGPL-3.0-or-later

{
    "name": "RotorDC Sale Address",
    "summary": """
        Display full address for invoice and delivery in sale order.""",
    "version": "12.0.1.0.0",
    "category": "Sales",
    "website": "https://coopiteasy.be",
    "author": "Coop IT Easy SC",
    "maintainers": ["carmenbianca"],
    "license": "AGPL-3",
    "application": False,
    "depends": ["sale"],
    "excludes": [],
    "data": [
        "views/sale_order_views.xml",
    ],
    "demo": [],
    "qweb": [],
}
