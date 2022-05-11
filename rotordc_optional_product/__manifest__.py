# Copyright 2022 Coop IT Easy SCRLfs
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "RotorDC Optional Product",
    "summary": """
        Custom modifications regarding RotorDC's use of optional products.""",
    "version": "12.0.1.0.0",
    "category": "Sales",
    "website": "https://coopiteasy.be",
    "author": "Coop IT Easy SCRLfs",
    "license": "AGPL-3",
    "application": False,
    "depends": [
        "sale",
        "web",
        "website_sale",
    ],
    "excludes": [],
    "data": [
        "views/assets.xml",
        "views/sale_product_configurator_templates.xml",
        "views/templates.xml",
    ],
    "demo": [],
    "qweb": [],
}
