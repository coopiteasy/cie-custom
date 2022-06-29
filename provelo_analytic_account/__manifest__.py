# Copyright 2021 Coop IT Easy SCRL fs
#   Robin Keunen <robin@coopiteasy.be>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
{
    "name": "Provelo Analytic Account",
    "version": "12.0.1.0.0",
    "depends": [
        "account",
        "hr",
        "resource_activity",
    ],
    "author": "Coop IT Easy SC",
    "license": "AGPL-3",
    "category": "",
    "website": "https://coopiteasy.be",
    "summary": """
        Match BOB analytical accounts.
    """,
    "data": [
        "security/ir.model.access.csv",
        "views/hr_department_views.xml",
        "views/provelo_financing_views.xml",
        "views/provelo_project_views.xml",
        "views/resource_location_views.xml",
        "views/account_invoice_views.xml",
        "views/resource_activity_type_views.xml",
        "views/actions.xml",
        "views/menus.xml",
    ],
    "installable": True,
}
