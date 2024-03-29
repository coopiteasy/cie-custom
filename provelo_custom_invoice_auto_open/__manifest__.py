# Copyright 2021 Coop IT Easy SCRL fs
#   Robin Keunen <robin@coopiteasy.be>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    "name": "Pro Velo Auto Open Invoices",
    "version": "12.0.1.0.0",
    "depends": [
        "sale",
        "resource_activity",
    ],
    "author": "Coop IT Easy SC",
    "license": "AGPL-3",
    "category": "Sales",
    "website": "https://coopiteasy.be",
    "summary": "Invoices are automatically opened for users "
    "with 'Automatically Open Invoices' group set.",
    "data": [
        "security/security.xml",
        "views/res_config_setting_views.xml",
    ],
    "installable": True,
}
