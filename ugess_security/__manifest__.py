# Copyright 2023 Akretion (http://www.akretion.com).
# @author Olivier Nibart <olivier.nibart@akretion.com>

{
    "name": "UGESS Security",
    "summary": """
    Security for UGESS.
    Mainly creates grocery roles and adapt the necessary stuff
    to make them work as needed.
    """,
    "version": "16.0.1.0.0",
    "author": "Akretion",  # pylint: disable=manifest-required-author
    "website": "https://coopiteasy.be",
    "license": "AGPL-3",
    "category": "Generic Modules",
    "depends": [
        # Odoo
        "account",
        "base",
        "contacts",
        "hr",
        "membership",
        "point_of_sale",
        "pos_loyalty",
        "pos_hr",
        "sale",
        "sales_team",
        "stock",
        "portal",
        # OCA
        "barcodes_generator_abstract",
        "base_export_manager",
        "base_location_district",
        "base_user_role",
        "membership_extension",
        "membership_withdrawal",
        "partner_contact_job_position",
        "partner_contact_personal_information_page",
        "pos_payment_change",
        "scrap_reason_code",
        "stock_change_qty_reason",
        "sql_request_abstract",
        # local-src
        "hr_pos_config_ids",
        # concerning this module please see it's manifest
        # for further thoughts.
        # We shoudl replace it eventually.
        "stock_settings_manager",
        # UGESS
        "ugess_membership",
        "ugess_partner_household",
        "ugess_partner_revenue",
        "ugess_partner_social_project",
        "ugess_supply_source",
        "document_knowledge",
    ],
    "data": [
        "security/ir_module_category.xml",
        "security/membership_security.xml",
        "security/res_district_security.xml",
        "security/res_partner_security.xml",
        "security/portal_security.xml",
        "security/res_users_roles.xml",
        "security/export_security.xml",
        "security/ir.model.access.csv",
        "views/res_partner_views.xml",
        "views/res_district_menus.xml",
        "views/members_menus.xml",
        "views/point_of_sale_menus.xml",
        "views/pos_loyalty_menus.xml",
        "views/sale_menus.xml",
    ],
    "installable": True,
    "application": False,
}
