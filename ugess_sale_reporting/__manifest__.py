{
    "name": "UGESS Sale Reporting",
    "summary": "Rapports ventes custom UGESS",
    "version": "16.0.1.0.0",
    "category": "Sales/Sales",
    "website": "https://coopiteasy.be",
    "author": "Akretion",  # pylint: disable=manifest-required-author
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "external_dependencies": {
        "python": [],
        "bin": [],
    },
    "depends": [
        "ugess_supply_source",
        "ugess_pricelist",
        "ugess_pos",
        "pos_sale_margin",
        "product_category_level",
    ],
    "data": [
        "report/report_sales_views.xml",
        "report/report_pos_order_views.xml",
    ],
    "demo": [],
    "qweb": [],
}
