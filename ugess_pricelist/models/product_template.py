# Copyright (C) 2023-Today GRAP (http://www.grap.coop)
# @author Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html


from odoo import api, fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    pricelist_item_ids = fields.One2many(
        comodel_name="product.pricelist.item",
        inverse_name="product_tmpl_id",
    )

    ugess_beneficiary_price = fields.Float(
        digits="Product Price",
        compute="_compute_ugess_price",
        store=True,
    )
    ugess_solidary_price = fields.Float(
        digits="Product Price",
        compute="_compute_ugess_price",
        store=True,
    )
    ugess_average_market_price = fields.Float(
        digits="Product Price",
        compute="_compute_ugess_price",
        store=True,
    )

    @api.depends(
        "pricelist_item_ids.fixed_price", "pricelist_item_ids.pricelist_id.ugess_type"
    )
    def _compute_ugess_price(self):
        for template in self:
            items = template.pricelist_item_ids
            beneficiary_items = items.filtered(
                lambda x: x.pricelist_id.ugess_type == "beneficiary"
            )
            template.ugess_beneficiary_price = (
                beneficiary_items and beneficiary_items[0].fixed_price or 0.0
            )

            solidary_items = items.filtered(
                lambda x: x.pricelist_id.ugess_type == "solidary"
            )
            template.ugess_solidary_price = (
                solidary_items and solidary_items[0].fixed_price or 0.0
            )

            average_market_items = items.filtered(
                lambda x: x.pricelist_id.ugess_type == "average_market"
            )
            template.ugess_average_market_price = (
                average_market_items and average_market_items[0].fixed_price or 0.0
            )
