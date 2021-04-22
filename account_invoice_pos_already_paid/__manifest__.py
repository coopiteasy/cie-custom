# -*- coding: utf-8 -*-
{
    "name": "Account invoice already paid",
    "summary": """
        Remove sentence about payment communication from invoice based on the account journal""",
    "description": """
        This module was developed to allow generated invoices from the Point of sale. Such invoices don't need to contain information about the payment, since the client has already paid. The point of sale is configured to use an account journal that has a new "Used for POS Invoice" flag turned on. To turn the flag on, edit a journal, open the Advanced Settings tab, and find the field under the Accounting App Options title.
    """,
    "author": "Coop IT Easy SCRLfs",
    "license": "AGPL-3",
    "category": "",
    "website": "https://www.coopiteasy.be",
    "version": "0.1",
    "depends": ["base", "account"],
    "data": [
        "views/view_account_journal_form.xml",
        "views/templates.xml",
    ],
}