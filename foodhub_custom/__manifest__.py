# Copyright 2019 Coop IT Easy SC
# 	    Robin Keunen <robin@coopiteasy.be>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Foodhub Custom",
    "version": "16.0.1.0.0",
    "summary": """
        Foodhub customizations""",
    "author": "Coop IT Easy SC",
    "website": "https://coopiteasy.be",
    "license": "AGPL-3",
    "category": "Account",
    "depends": [
        "sale",
        "sale_stock",
        "website_sale_stock",
        "sale_order_volume",
    ],
    "data": ["reports/report_deliveryslip.xml", "views/templates.xml"],
}
