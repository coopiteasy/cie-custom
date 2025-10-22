# Copyright (C) 2022-Today GRAP (http://www.grap.coop)
# @author Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

{
    "name": "UGESS - Custom Labels",
    "summary": "Implement pricetags for UGESS",
    "version": "16.0.1.0.0",
    "category": "Point of Sale",
    "maintainers": ["legalsylvain"],
    "author": "GRAP",  # pylint: disable=manifest-required-author
    "website": "https://coopiteasy.be",
    "license": "AGPL-3",
    "depends": [
        # Odoo
        "product",
        # OCA
        "report_label",
        "product_print_category",
        # Custom
        "ugess_supply_source",
        "ugess_pricelist",
    ],
    "data": [
        "data/template_product_agipa_65.xml",
        "data/template_product_label_ugess_1.xml",
        "data/report_paperformat.xml",
        "data/report_paperformat_label.xml",
        "data/ir_actions_server.xml",
        "data/product_print_category.xml",
    ],
    "demo": [
        "demo/product_tag.xml",
        "demo/res_partner.xml",
        "demo/product_product.xml",
    ],
    "installable": True,
}
