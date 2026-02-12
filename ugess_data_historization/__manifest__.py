{
    "name": "UGESS - Data Historization",
    "version": "16.0.0.0.1",
    "author": "GRAP",  # pylint: disable=manifest-required-author
    "website": "https://coopiteasy.be",
    "license": "AGPL-3",
    "category": "Generic Modules",
    "depends": [
        # Odoo
        "base",
        # OCA
        "partner_contact_job_position",
        "partner_contact_gender",
        # custom
        "ugess_partner_household",
        "ugess_partner_revenue",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/view_data_historization_res_partner.xml",
        "views/view_data_historization_household_member.xml",
        "views/view_res_partner.xml",
    ],
    "installable": True,
}
