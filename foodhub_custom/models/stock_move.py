# Copyright 2020 Coop IT Easy SCRL fs
#   Robin Keunen <robin@coopiteasy.be>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class StockMove(models.Model):
    _inherit = "stock.move"

    order_line_id = fields.Many2one(
        comodel_name="sale.order.line",
        string="Related Sale Line",
        compute="_compute_order_line_id",
        store=True,
    )

    @api.depends("picking_id.origin")
    def _compute_order_line_id(self):
        for move in self:
            origin = move.picking_id.origin
            sale_order = self.env["sale.order"].search([("name", "=", origin)])
            order_line = sale_order.order_line.filtered(
                lambda line: line.product_id == move.product_id
            )
            move.order_line_id = order_line[0] if order_line else order_line
