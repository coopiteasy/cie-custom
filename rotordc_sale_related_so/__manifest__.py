# SPDX-FileCopyrightText: 2022 Coop IT Easy SC
#
# SPDX-License-Identifier: AGPL-3.0-or-later

{
    "name": "RotorDC Sale Linked SO",
    "summary": """
        Adds M2M links between SOs.""",
    "version": "12.0.1.0.0",
    "category": "Warehouse",
    "website": "https://coopiteasy.be",
    "author": "Coop IT Easy SC",
    "maintainers": ["robinkeunen"],
    "license": "AGPL-3",
    "application": False,
    "depends": [
        "sale_stock",
    ],
    "excludes": [],
    "data": [
        "views/sale_order_views.xml",
        "views/stock_picking_views.xml",
        "security/ir.model.access.csv",
    ],
    "demo": [],
    "qweb": [],
}
