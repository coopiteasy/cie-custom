# Copyright 2022 Akretion (https://www.akretion.com).
# @author Pierrick Brun <pierrick.brun@akretion.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class StockPicking(models.Model):
    _inherit = "stock.picking"

    reason_code_id = fields.Many2one(
        "scrap.reason.code", states={"done": [("readonly", True)]}
    )
    is_scrap_picking = fields.Boolean(compute="_compute_is_scrap_picking")

    @api.depends("location_dest_id.scrap_location")
    def _compute_is_scrap_picking(self):
        for record in self:
            if record.location_dest_id:
                record.is_scrap_picking = record.location_dest_id.scrap_location
            else:
                record.is_scrap_picking = False
