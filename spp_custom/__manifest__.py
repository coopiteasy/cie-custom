# Copyright 2019 Coop IT Easy SCRL fs
#   Robin Keunen <robin@coopiteasy.be>
#   Houssine Bakkali <houssine@coopiteasy.be>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
{
    "name": "SPP Customizations",
    "version": "12.0.1.1.0",
    "depends": ["beesdoo_base", "beesdoo_product"],
    "author": "Coop IT Easy SC",
    "license": "AGPL-3",
    "category": "",
    "website": "https://coopiteasy.be",
    "summary": """
        Specifics customizations for SPP
    """,
    "data": [
        "data/product_sequence.xml",
        "templates/pos_templates.xml",
        "views/account_invoice.xml",
        "views/product.xml",
        "views/product_supplierinfo_views.xml",
        "views/purchase_order.xml",
        "views/res_partner.xml",
        "views/sale_order.xml",
        "views/stock_picking.xml",
    ],
    "qweb": ["static/src/xml/pos.xml"],
    "installable": True,
}
