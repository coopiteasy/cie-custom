# SPDX-FileCopyrightText: 2023 Coop IT Easy SC
#
# SPDX-License-Identifier: AGPL-3.0-or-later

{
    "name": "SAWB Custom : Hide VAT for Individual",
    "summary": """
        Hide the partner's VAT field if the partner is an individual.""",
    "version": "16.0.1.0.0",
    "category": "Contact",
    "website": "https://coopiteasy.be",
    "author": "Coop IT Easy SC",
    "maintainers": ["victor-champonnois"],
    "license": "AGPL-3",
    "depends": [
        "base",
    ],
    "data": [
        "views/res_partner_view.xml",
    ],
}
