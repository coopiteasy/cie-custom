# SPDX-FileCopyrightText: 2026 Coop IT Easy SC
#
# SPDX-License-Identifier: AGPL-3.0-or-later

{
    "name": "Accompagner Custom",
    "summary": "Custom module for Accompagner",
    "version": "18.0.1.0.0",
    "category": "Customer Relationship Management",
    "website": "https://github.com/coopiteasy/cie-custom",
    "author": "Coop IT Easy SC",
    "maintainers": ["mihien"],
    "license": "AGPL-3",
    "depends": [
        "account",
        "base",
        "base_geolocalize",
        "contacts",
        "donation_base",
        "fieldservice",
        "partner_contact_personal_information_page",
        "website",
    ],
    "data": [
        "security/ir.model.access.csv",
        "security/accompagner_custom_security.xml",
        "views/partner_social_configuration_views.xml",
        "views/res_partner_views.xml",
    ],
}
