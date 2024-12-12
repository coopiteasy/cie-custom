# Copyright 2020 Coop IT Easy SCRL fs
#   Robin Keunen <robin@coopiteasy.be>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class StockMove(models.Model):
    _inherit = "stock.move"
    _order = "product_category,product_default_code"

    product_category = fields.Many2one(related="product_id.categ_id", store=True)
    product_default_code = fields.Char(related="product_id.default_code", store=True)
