# Copyright 2019 Coop IT Easy SCRL fs
#   Robin Keunen <robin@coopiteasy.be>
#   Houssine Bakkali <houssine@coopiteasy.be>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
{
    "name": "SPP Customizations",
    "version": "12.0.1.0.1",
    "depends": ["account", "beesdoo_base", "beesdoo_product", "point_of_sale"],
    "author": "Coop IT Easy SCRLfs",
    "license": "AGPL-3",
    "category": "",
    "website": "https://www.coopiteasy.be",
    "summary": """
        Specifics customizations for SPP
    """,
    "data": [
        "security/ir.model.access.csv",
        "data/product_sequence.xml",
        "views/product.xml",
    ],
    "installable": True,
}
