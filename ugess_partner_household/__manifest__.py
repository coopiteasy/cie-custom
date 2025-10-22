# SPDX-FileCopyrightText: 2022 Coop IT Easy SC
#
# SPDX-License-Identifier: AGPL-3.0-or-later

{
    "name": "UGESS Partner Household",
    "summary": """
        Create a household model related to a partner.""",
    "version": "16.0.0.0.0",
    "category": "Uncategorized",
    "website": "https://coopiteasy.be",
    "author": "Coop IT Easy SC",
    "license": "AGPL-3",
    "application": False,
    "depends": [
        "membership",
        "ugess_partner_revenue",
        "partner_contact_gender",
        "partner_contact_birthdate",
        "partner_contact_job_position",
        "partner_contact_personal_information_page",
    ],
    "excludes": [],
    "data": [
        "security/ir_module_category.xml",
        "security/res_groups.xml",
        "security/ir.model.access.csv",
        "views/menu.xml",
        "views/res_partner_view.xml",
        "views/household_member_view.xml",
        "views/household_situation_view.xml",
        "data/ir_cron.xml",
    ],
    "demo": [
        "demo/household_situation.xml",
        "demo/res_partner_job_position.xml",
        "demo/res_partner.xml",
        "demo/household_member.xml",
    ],
    "qweb": [],
    "post_init_hook": "post_init_hook",
}
