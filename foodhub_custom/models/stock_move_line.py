# Copyright 2020 Coop IT Easy SCRL fs
#   Robin Keunen <robin@coopiteasy.be>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class StockMoveLine(models.Model):
    _inherit = "stock.move.line"

    order_line_id = fields.Many2one(
        comodel_name="sale.order.line",
        string="Related Sale Line",
        compute="_compute_order_line_id",
        store=True,
    )

    @api.multi
    @api.depends("picking_id.origin")
    def _compute_order_line_id(self):
        for move_line in self:
            origin = move_line.picking_id.origin
            sale_order = self.env["sale.order"].search([("name", "=", origin)])
            order_line = sale_order.order_line.filtered(
                lambda line: line.product_id == move_line.product_id
            )
            move_line.order_line_id = order_line[0] if order_line else order_line
