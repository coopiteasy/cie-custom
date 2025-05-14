# SPDX-FileCopyrightText: 2025 Coop IT Easy SC
#
# SPDX-License-Identifier: AGPL-3.0-or-later

{
    "name": "LPCR Donation Tax Report",
    "summary": "Custom tax report for donation",
    "version": "16.0.1.0.0",
    "category": "Accounting",
    "website": "https://coopiteasy.be",
    "author": "Coop IT Easy SC",
    "maintainers": ["remytms"],
    "license": "AGPL-3",
    "depends": ["donation_base", "l10n_fr_siret", "board_signature"],
    "data": [
        "report/report_donationtax.xml",
    ],
}
