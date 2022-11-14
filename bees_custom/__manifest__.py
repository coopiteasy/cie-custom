# Copyright 2021 Coop IT Easy SCRL fs
#   Robin Keunen <robin@coopiteasy.be>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
{
    "name": "BEES Customizations",
    "version": "12.0.1.1.0",
    "depends": [
        "point_of_sale",
        "account_invoice_date_required",
        "beesdoo_product_info_screen",
        "pos_mail_receipt",
    ],
    "author": "Coop IT Easy SC",
    "license": "AGPL-3",
    "category": "Custom",
    "website": "https://coopiteasy.be",
    "summary": """
        Specifics customizations for BEES coop.
    """,
    "data": [
        "views/account_invoice.xml",
        "views/products.xml",
        "data/default_barcode_pattern.xml",
    ],
    "installable": True,
}
