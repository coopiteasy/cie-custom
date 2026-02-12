{
    "name": "Vues personnalisées UGESS",
    "version": "16.0.0.0.1",
    "author": "Akretion",  # pylint: disable=manifest-required-author
    "website": "https://coopiteasy.be",
    "license": "AGPL-3",
    "category": "Generic Modules",
    "depends": [
        "ugess_base",
        "ugess_membership",
        "ugess_partner_household",
        "ugess_partner_revenue",
        "ugess_partner_social_project",
        "product",
        "sale",
        "partner_contact_personal_information_page",
    ],
    "installable": True,
    "application": False,
    "data": [
        "views/product_views.xml",
        "views/picking_views.xml",
        "views/res_partner_views.xml",
    ],
}
