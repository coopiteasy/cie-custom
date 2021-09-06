# Copyright 2020 Coop IT Easy SCRL fs
#   Robin Keunen <robin@coopiteasy.be>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class StockPicking(models.Model):
    _inherit = "stock.picking"

    sale_order_id = fields.Many2one(
        comodel_name="sale.order",
        string="Sale Order",
        compute="_compute_sale_order_id",
    )
    volume = fields.Float(string="Order Volume (m³)", compute="_compute_sale_order_id")

    @api.model
    @api.depends("origin")
    def _compute_sale_order_id(self):
        for picking in self:
            sale_order = self.env["sale.order"].search([("name", "=", picking.origin)])
            # trigger
            sale_order._compute_order_volume()
            sale_order.compute_product_category_volumes()

            picking.sale_order_id = sale_order
            picking.volume = sale_order.volume
