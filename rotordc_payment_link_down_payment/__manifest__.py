# SPDX-FileCopyrightText: 2022 Coop IT Easy SC
#
# SPDX-License-Identifier: AGPL-3.0-or-later

{
    "name": "RotorDC Payment Link Down Payment",
    "summary": """
        Register payments done with payment acquirers as down payment on sale
        orders.""",
    "version": "12.0.1.0.0",
    "category": "Sales",
    "website": "https://coopiteasy.be",
    "author": "Coop IT Easy SC",
    "maintainers": ["carmenbianca"],
    "license": "AGPL-3",
    "application": False,
    "depends": [
        "payment",
        "sale_down_payment",
    ],
    "excludes": [],
    "data": [],
    "demo": [],
    "qweb": [],
}
