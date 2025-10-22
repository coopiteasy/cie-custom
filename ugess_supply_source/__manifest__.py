{
    "name": "UGESS Supply Source",
    "summary": "add notion of supply source on product and pickings",
    "version": "16.0.1.0.0",
    "category": "Stock",
    "website": "https://coopiteasy.be",
    "author": "Akretion",  # pylint: disable=manifest-required-author
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "stock",
    ],
    "data": [
        "views/supply_source_views.xml",
        "views/product_views.xml",
        "views/picking_views.xml",
        "security/ir.model.access.csv",
    ],
}
