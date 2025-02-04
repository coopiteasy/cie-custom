import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class StockMove(models.Model):
    _inherit = "stock.move"

    product_category_name = fields.Char(
        related="product_id.categ_id.complete_name",
        store=True,
        string="Product Category",
    )
