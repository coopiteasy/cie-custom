# SPDX-FileCopyrightText: 2022 Coop IT Easy SC
#
# SPDX-License-Identifier: AGPL-3.0-or-later

{
    "name": "SPP Point of Sale Mustard",
    "summary": """
        Make a button in the POS interface mustard-coloured.""",
    "version": "12.0.1.0.0",
    "category": "Point of Sale",
    "website": "https://coopiteasy.be",
    "author": "Coop IT Easy SC",
    "maintainers": ["carmenbianca"],
    "license": "AGPL-3",
    "application": False,
    "depends": [
        "pos_shift_partner_can_shop",
    ],
    "excludes": [],
    "data": [
        "views/assets.xml",
    ],
    "demo": [],
    "qweb": [],
}
