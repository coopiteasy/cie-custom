# Copyright 2023 Akretion (http://www.akretion.com).
# @author Olivier Nibart <olivier.nibart@akretion.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "UGESS Security User Stats",
    "summary": """
    Security for UGESS specific to Stats profiles.

    This module is intended to set a user which rights will be pretty
    much restricted to some anonymized stats.

    To be able to achieve that whithout using an external user,
    which would have required developping portal views,
    there is here a hack to resctrict the right of the internal users.

    Therefore, it is mandatory to add another low level group to real interna users :
    ugess_security_user_stats.group_user_all_non_private_contacts
    """,
    "version": "16.0.1.0.0",
    "author": "Akretion",  # pylint: disable=manifest-required-author
    "website": "https://coopiteasy.be",
    "license": "AGPL-3",
    "category": "Generic Modules",
    "depends": [
        # Odoo
        "base",
        "mail",
        "hr",
        "spreadsheet_dashboard",
        # OCA
        "sql_request_abstract",
        # UGESS
        "ugess_security",
    ],
    "data": [
        "security/security_hack.xml",
        "security/res_users_roles.xml",
        "security/sql_request_abstract_security.xml",
        "views/view_bi_sql_view.xml",
        "views/spreadsheet_dashboard.xml",
        "views/base_menu.xml",
    ],
    "post_init_hook": "post_init_hook",
    "uninstall_hook": "uninstall_hook",
    "installable": True,
    "application": False,
}
