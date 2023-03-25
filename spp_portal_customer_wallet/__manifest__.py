# SPDX-FileCopyrightText: 2023 Coop IT Easy SC
#
# SPDX-License-Identifier: AGPL-3.0-or-later

{
    "name": "SPP Portal Customer Wallet",
    "summary": """
        On the user's home page, display information about customer wallet usage.""",
    "version": "12.0.1.0.0",
    "category": "Accounting & Finance",
    "website": "https://coopiteasy.be",
    "author": "Coop IT Easy SC",
    "maintainers": ["carmenbianca"],
    "license": "AGPL-3",
    "application": False,
    "depends": [
        "spp_custom",
        "pos_customer_wallet",
        "portal",
        "website",
    ],
    "excludes": [],
    "data": [
        "views/portal_templates.xml",
    ],
    "demo": [],
    "qweb": [],
}
