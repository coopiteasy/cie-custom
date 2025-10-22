# Copyright 2023 Akretion (https://www.akretion.com).
# @author Pierrick Brun <pierrick.brun@akretion.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class StockMove(models.Model):
    _inherit = "stock.move"

    weight = fields.Float(compute="_compute_weight")

    @api.depends("product_id.weight", "product_uom", "product_uom_qty")
    def _compute_weight(self):
        for record in self:
            record.weight = record.product_id.weight * record.product_uom_qty
