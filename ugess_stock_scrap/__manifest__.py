{
    "name": "UGESS Stock Scrap",
    "summary": "UGESS custom scraping process",
    "version": "16.0.1.0.0",
    "category": "Warehouse Management",
    "website": "https://coopiteasy.be",
    "author": "Akretion",  # pylint: disable=manifest-required-author
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "scrap_reason_code",
    ],
    "data": ["views/stock_scrap_views.xml", "views/picking_views.xml"],
}
