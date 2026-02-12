# Copyright (C) 2022-Today GRAP (http://www.grap.coop)
# @author Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

{
    "name": "UGESS - Point of Sale custom features",
    "summary": "Implement custom features for UGESS",
    "version": "16.0.1.0.0",
    "category": "Point of Sale",
    "maintainers": ["legalsylvain"],
    "author": "GRAP",  # pylint: disable=manifest-required-author
    "website": "https://coopiteasy.be",
    "license": "AGPL-3",
    "depends": [
        # Odoo
        "point_of_sale",
        # OCA
        "pos_membership",
        "pos_discount_all",
        # Ugess
        "ugess_membership",
        "ugess_partner_household",
    ],
    "assets": {
        "point_of_sale.assets": [
            "ugess_pos/static/src/js/PaymentScreen.js",
            "ugess_pos/static/src/js/models.js",
            "ugess_pos/static/src/xml/PartnerDetailsEdit.xml",
            "ugess_pos/static/src/xml/PartnerLine.xml",
            "ugess_pos/static/src/xml/OrderSummary.xml",
            "ugess_pos/static/src/xml/OrderReceipt.xml",
            "ugess_pos/static/src/xml/PaymentScreen.xml",
            "ugess_pos/static/src/css/ugess_pos.scss",
        ],
    },
    "demo": [],
    "installable": True,
}
