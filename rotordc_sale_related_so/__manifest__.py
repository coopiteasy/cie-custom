# SPDX-FileCopyrightText: 2022 Coop IT Easy SC
#
# SPDX-License-Identifier: AGPL-3.0-or-later

{
    "name": "RotorDC Sale Linked SO",
    "summary": "Add M2M links between SOs",
    "version": "16.0.1.0.0",
    "category": "Sales/Sales",
    "website": "https://coopiteasy.be",
    "author": "Coop IT Easy SC",
    "maintainers": ["robinkeunen"],
    "license": "AGPL-3",
    "depends": [
        "sale_stock",
        "rotordc_report_picking_huge_sale_order",
    ],
    "data": [
        "views/sale_order_views.xml",
        "views/stock_picking_views.xml",
        "report/report_stockpicking_operations.xml",
        "security/ir.model.access.csv",
    ],
}
