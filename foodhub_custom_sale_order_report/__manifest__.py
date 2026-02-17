# SPDX-FileCopyrightText: 2026 Coop IT Easy SC
#
# SPDX-License-Identifier: AGPL-3.0-or-later

{
    "name": "Foodhub Custom Sale Order Report",
    "summary": "add base_unit_price and rename Unit Price to Box Price",
    "version": "16.0.1.0.0",
    "category": "Sales",
    "website": "https://coopiteasy.be",
    "author": "Coop IT Easy SC",
    "maintainers": ["mihien"],
    "license": "AGPL-3",
    "depends": [
        "sale",
        "website_sale",
    ],
    "data": ["reports/ir_actions_report_templates.xml"],
}
