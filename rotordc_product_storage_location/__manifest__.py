# SPDX-FileCopyrightText: 2022 Coop IT Easy SC
#
# SPDX-License-Identifier: AGPL-3.0-or-later

{
    "name": "RotorDC Product Storage Location",
    "summary": """
        Select a storage location on products.""",
    "version": "12.0.1.0.0",
    "category": "Sales",
    "website": "https://coopiteasy.be",
    "author": "Coop IT Easy SC",
    "maintainers": ["carmenbianca"],
    "license": "AGPL-3",
    "application": False,
    "depends": [
        "product",
        "stock",
    ],
    "excludes": [],
    "data": [
        "security/ir.model.access.csv",
        "views/product_template_views.xml",
        "report/report_stockpicking_operations.xml",
    ],
    "demo": [],
    "qweb": [],
}
