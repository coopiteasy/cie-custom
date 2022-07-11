# SPDX-FileCopyrightText: 2022 Coop IT Easy SC
#
# SPDX-License-Identifier: AGPL-3.0-or-later

{
    "name": "RotorDC Sale Picking State",
    "summary": """
        Set states for stock pickings on sale orders depending on the stock
        pickings' types.""",
    "version": "12.0.1.0.0",
    "category": "Warehouse",
    "website": "https://coopiteasy.be",
    "author": "Coop IT Easy SC",
    "maintainers": ["carmenbianca"],
    "license": "AGPL-3",
    "application": False,
    "depends": [
        "sale_stock",
    ],
    "excludes": [],
    "data": [
        "views/sale_order_views.xml",
    ],
    "demo": [],
    "qweb": [],
}
