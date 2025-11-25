# SPDX-FileCopyrightText: 2025 Coop IT Easy SC
#
# SPDX-License-Identifier: AGPL-3.0-or-later

{
    "name": "LPCR Website Partner Form",
    "summary": "Add a form to add partners from website.",
    "version": "16.0.1.0.2",
    "category": "website",
    "website": "https://coopiteasy.be",
    "author": "Coop IT Easy SC",
    "maintainers": ["remytms"],
    "license": "AGPL-3",
    "depends": [
        "website",
        "contacts",
        "l10n_fr_siret",
        "partner_firstname",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/res_partner_views.xml",
        "views/res_partner_customer_type_views.xml",
        "views/res_partner_acquisition_medium_views.xml",
    ],
    "assets": {
        "web.assets_frontend": [
            "lpcr_website_partner_form/static/src/js/s_website_form_snippets.esm.js",
        ],
    },
}
