{
    "name": "UGESS partner revenue",
    "version": "16.0.0.0.1",
    "author": "Coop IT Easy SC",
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
        "views/social_budget_move_view.xml",
        "views/social_budget_move_category_view.xml",
    ],
    "demo": ["demo/social_budget_move_category.xml"],
    "installable": True,
    "application": False,
}
