# Copyright 2022 Akretion (https://www.akretion.com).
# @author Pierrick Brun <pierrick.brun@akretion.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class StockPicking(models.Model):
    _inherit = "stock.picking"

    supply_source_id = fields.Many2one(
        "supply.source",
    )


class StockMove(models.Model):
    _inherit = "stock.move"

    supply_source_id = fields.Many2one(
        "supply.source",
        related="picking_id.supply_source_id",
        # ONI: this is to allow grouping on view
        # to be checked against perf. issues
        store=True,
    )
