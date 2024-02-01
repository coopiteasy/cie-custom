# SPDX-FileCopyrightText: 2022 Coop IT Easy SC
#
# SPDX-License-Identifier: AGPL-3.0-or-later

{
    "name": "Foodhub Custom Product Kanban View",
    "summary": """
        Adapt the kanban view for product""",
    "version": "14.0.1.0.0",
    "category": "Product",
    "website": "https://coopiteasy.be",
    "author": "Coop IT Easy SC",
    "maintainers": ["remytms"],
    "license": "AGPL-3",
    "application": False,
    "depends": ["product", "stock"],
    "excludes": [],
    "data": [
        "views/product_template_views.xml",
        "views/stock_product_views.xml",
    ],
    "demo": [],
    "qweb": [],
}
