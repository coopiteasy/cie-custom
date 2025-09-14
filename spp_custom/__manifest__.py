# Copyright 2019 Coop IT Easy SCRL fs
#   Robin Keunen <robin@coopiteasy.be>
#   Houssine Bakkali <houssine@coopiteasy.be>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
{
    "name": "SPP Customizations",
    "author": "Coop IT Easy SC",
    "license": "AGPL-3",
    "category": "",
    "website": "https://coopiteasy.be",
    "summary": """
        Specifics customizations for SPP
    """,
    "version": "16.0.1.0.0",
    "depends": [
        "barcodes_generator_product",
        "beesdoo_product_label",
        "product",
        "spp_pos_mustard",
        "stock_inventory",
    ],
    "data": [
        "data/product_sequence.xml",
        "views/account_move_views.xml",
        "views/product_supplierinfo_views.xml",
        "views/product_template_views.xml",
        "views/purchase_views.xml",
        "views/res_partner_views.xml",
        "views/sale_order_views.xml",
        "views/stock_picking_views.xml",
        "views/stock_move_views.xml",
    ],
    "qweb": ["static/src/xml/pos.xml"],
    "assets": {
        "point_of_sale.assets": [
            "spp_custom/static/src/css/Screens/ReceiptScreen/OrderReceipt.scss",
            "spp_custom/static/src/js/models.esm.js",
            "spp_custom/static/src/xml/Screens/ReceiptScreen/OrderReceipt.xml",
        ],
    },
}
