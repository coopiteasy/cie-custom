# SPDX-FileCopyrightText: 2025 Coop IT Easy SC
#
# SPDX-License-Identifier: AGPL-3.0-or-later

{
    "name": "LPCR Donation Tax Report",
    "summary": "Custom tax report for donation",
    "version": "16.0.2.0.0",
    "category": "Accounting",
    "website": "https://coopiteasy.be",
    "author": "Coop IT Easy SC",
    "maintainers": ["remytms"],
    "license": "AGPL-3",
    "depends": [
        "board_signature",
        "donation",
        "l10n_fr_siret",
        "pos_donation",
    ],
    "data": [
        "report/report_donation_tax.xml",
        "views/donation_tax_receipt.xml",
        "views/donation_donation_views.xml",
        "views/res_partner.xml",
        "wizards/tax_receipt_annual_create_view.xml",
    ],
}
