import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class StockMove(models.Model):
    _inherit = "stock.move"
    _order = "product_category_name,product_default_code"

    product_default_code = fields.Char(
        related="product_id.default_code",
        store=True,
        string="Internal Reference",
    )

    product_category_name = fields.Char(
        related="product_id.categ_id.complete_name",
        store=True,
        string="Product Category",
    )
