# Copyright (C) 2022-Today GRAP (http://www.grap.coop)
# @author Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

{
    "name": "UGESS - Custom Pricelist",
    "summary": "Implement extra fields for UGESS Pricelists",
    "version": "16.0.1.0.0",
    "category": "Custom",
    "maintainers": ["legalsylvain"],
    "author": "GRAP",  # pylint: disable=manifest-required-author
    "website": "https://coopiteasy.be",
    "license": "AGPL-3",
    "depends": [
        # Odoo
        "product",
    ],
    "data": ["views/view_product_pricelist.xml"],
    "demo": [
        "demo/product_product.xml",
        "demo/product_pricelist.xml",
    ],
    "installable": True,
}
