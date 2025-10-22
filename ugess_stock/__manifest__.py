{
    "name": "UGESS Stock",
    "summary": "UGESS stock custom",
    "version": "16.0.1.0.0",
    "category": "Warehouse Management",
    "website": "https://coopiteasy.be",
    "author": "Akretion",  # pylint: disable=manifest-required-author
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "stock",
        "ugess_supply_source",
    ],
    "data": [
        "views/stock_views.xml",
        "views/picking_views.xml",
        "views/stock_menus.xml",
    ],
}
