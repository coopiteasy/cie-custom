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
            # No stock picking found.
            ("none", _("None")),
            # Multiple conflicting found.
            ("unknown", _("Unknown")),
            # Same as states on stock.picking.
            # FIXME: Should we dynamically create these from stock.picking? What
            # about translations?
            ("draft", _("Draft")),
            ("waiting", _("Waiting Another Operation")),
            ("confirmed", _("Waiting")),
            ("assigned", _("Ready")),
            ("done", _("Done")),
            ("cancel", _("Cancelled")),
        ]

    @api.depends(
        "picking_ids.picking_type_code",
        "picking_ids.state",
    )
    def _compute_picking_states(self):
        for order in self:
            # Map picking_type_codes to states.
            code_mapping = {}
            conflicts = set()
            for picking in order.picking_ids:
                # The picking's state is either the first detected state for a
                # given code, or the same state has been encountered before for
                # that code.
                if picking.picking_type_code not in code_mapping:
                    code_mapping[picking.picking_type_code] = picking.state
                # picking_type_code has conflicting states.
                if code_mapping[picking.picking_type_code] != picking.state:
                    conflicts.add(picking.picking_type_code)
            for code, attr in zip(
                ("internal", "outgoing"),
                ("internal_picking_state", "outgoing_picking_state"),
            ):
                if code in conflicts:
                    setattr(order, attr, "unknown")
                elif code not in code_mapping:
                    setattr(order, attr, "none")
                else:
                    # FIXME: What happens if we try to set an unsupported state?
                    setattr(order, attr, code_mapping[code])

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
