# SPDX-FileCopyrightText: 2022 Coop IT Easy SC
#
# SPDX-License-Identifier: AGPL-3.0-or-later

{
    "name": "RotorDC Sale Invoice Comment",
    "summary": """
        Make sure that the terms & conditions are always set on all invoices,
        and don't display the reference on POS invoices.""",
    "version": "12.0.1.0.0",
    "category": "Sales",
    "website": "https://coopiteasy.be",
    "author": "Coop IT Easy SC",
    "maintainers": ["carmenbianca"],
    "license": "AGPL-3",
    "application": False,
    "depends": [
        "account",
        "sale",
    ],
    "excludes": [],
    "data": [
        "views/report_invoice.xml",
    ],
    "demo": [],
    "qweb": [],
}
