# SPDX-FileCopyrightText: 2022 Coop IT Easy SC
#
# SPDX-License-Identifier: AGPL-3.0-or-later

from odoo import api, fields, models
from odoo.tools.translate import _


class SaleOrder(models.Model):
    _inherit = "sale.order"

    @api.model
    def get_picking_state_selection(self):
        return [
            ("unknown", _("Unknown")),
            ("unprocessed", _("Unprocessed")),
            ("done", _("Done")),
        ]

    @api.depends(
        "picking_ids.picking_type_code",
        "picking_ids.state",
    )
    def _compute_picking_states(self):
        for order in self:
            # Map picking_type_codes to picking_ids. We should only have one of
            # each.
            code_mapping = {}
            duplicates = set()
            for picking in order.picking_ids:
                # picking is first with that picking_type_code
                if (
                    code_mapping.setdefault(picking.picking_type_code, picking)
                    == picking
                ):
                    continue
                # picking_type_code was already used by another picking
                else:
                    duplicates.add(picking.picking_type_code)
            for code, attr in zip(
                ("internal", "outgoing"),
                ("internal_picking_state", "outgoing_picking_state"),
            ):
                if code in duplicates or code not in code_mapping:
                    setattr(order, attr, "unknown")
                else:
                    if code_mapping[code].state == "done":
                        setattr(order, attr, "done")
                    else:
                        setattr(order, attr, "unprocessed")

    internal_picking_state = fields.Selection(
        string="Internal Picking State",
        selection="get_picking_state_selection",
        compute=_compute_picking_states,
        store=True,
    )
    outgoing_picking_state = fields.Selection(
        string="Delivery State",
        selection="get_picking_state_selection",
        compute=_compute_picking_states,
        store=True,
    )
