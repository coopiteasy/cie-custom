# Copyright 2021 Coop IT Easy SCRL fs
#   Robin Keunen <robin@coopiteasy.be>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    "name": "Account invoice already paid",
    "summary": """Remove sentence about payment communication from invoice
    based on the account journal""",
    "author": "Coop IT Easy SC",
    "license": "AGPL-3",
    "category": "",
    "website": "https://coopiteasy.be",
    "version": "12.0.1.0.0",
    "depends": ["base", "account"],
    "data": [
        "views/view_account_journal_form.xml",
        "views/templates.xml",
    ],
}
