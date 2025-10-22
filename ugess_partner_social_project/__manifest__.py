{
    "name": "UGESS Partner Social Project",
    "version": "16.0.0.0.1",
    "author": "Akretion",  # pylint: disable=manifest-required-author
    "website": "https://coopiteasy.be",
    "license": "AGPL-3",
    "category": "Generic Modules",
    "depends": [
        "membership",
        "contacts",
        "partner_contact_personal_information_page",
    ],
    "data": [
        "security/ir_module_category.xml",
        "security/res_groups.xml",
        "security/ir.model.access.csv",
        "views/res_partner_view.xml",
        "views/social_project_type_view.xml",
        "views/social_project_views.xml",
    ],
    "installable": True,
    "application": False,
}
