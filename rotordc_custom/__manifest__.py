# Copyright 2022 Coop IT Easy SC
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "rotordc_custom",
    "summary": "Customization for RotorDC",
    "version": "16.0.1.0.0",
    "category": "Uncategorized",
    "website": "https://coopiteasy.be",
    "author": "Coop IT Easy SC",
    "license": "AGPL-3",
    "depends": [
        "product",
        "website_sale",
        "website_sale_stock",
        "website_sale_product_weight",
    ],
    "data": [
        "reports/product_reports.xml",
        "reports/product_template_templates.xml",
        "reports/product_product_templates.xml",
        "views/templates.xml",
    ],
    "assets": {
        "web.assets_frontend": [
            "rotordc_custom/static/src/**/*",
        ],
    },
}
