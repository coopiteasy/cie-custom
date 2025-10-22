{
    "name": "Données statiques UGESS",
    "version": "16.0.0.0.1",
    "author": "Akretion",  # pylint: disable=manifest-required-author
    "website": "https://coopiteasy.be",
    "license": "AGPL-3",
    "category": "Generic Modules",
    "depends": [
        "ugess_base",
        "ugess_stock_scrap",
    ],
    "installable": True,
    "application": False,
    "data": [
        "product.category.csv",
        "pos.category.csv",
        "res.partner.job_position.csv",
        "social.budget.move.category.csv",
        "household.situation.csv",
        "social.project.type.csv",
        "supply.source.csv",
        "scrap.reason.code.csv",
    ],
}
