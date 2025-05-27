# SPDX-FileCopyrightText: 2025 Coop IT Easy SC
#
# SPDX-License-Identifier: AGPL-3.0-or-later

{
    "name": "LPCR POS Membership",
    "summary": "POS Membership customizations for LPCR",
    "version": "16.0.1.0.0",
    "category": "Point of Sale",
    "website": "https://coopiteasy.be",
    "author": "Coop IT Easy SC",
    "maintainers": ["flaenen"],
    "license": "AGPL-3",
    "depends": ["pos_membership_delegated_partner"],
    "assets": {
        "point_of_sale.assets": [
            "lpcr_pos_membership/static/src/css/lpcr_pos_membership.css",
            "lpcr_pos_membership/static/src/xml/*.xml",
            "lpcr_pos_membership/static/src/js/*.js",
        ],
    },
}
