import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    product_category_name = fields.Char(
        related="product_id.categ_id.complete_name",
        store=True,
        string="Product Category",
    )
