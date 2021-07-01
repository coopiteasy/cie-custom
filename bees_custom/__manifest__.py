# Copyright 2021 Coop IT Easy SCRL fs
#   Robin Keunen <robin@coopiteasy.be>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
{
    "name": "BEES Customizations",
    "version": "12.0.1.0.1",
    "depends": [
        "beesdoo_account",
        "beesdoo_product_info_screen",
    ],
    "author": "Coop IT Easy SCRLfs",
    "license": "AGPL-3",
    "category": "Custom",
    "website": "https://www.coopiteasy.be",
    "summary": """
        Specifics customizations for BEES coop.
    """,
    "data": [
        "views/account_invoice.xml",
        "views/products.xml",
    ],
    "installable": True,
}
