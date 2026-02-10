# SPDX-FileCopyrightText: 2026 Coop IT Easy SC
#
# SPDX-License-Identifier: AGPL-3.0-or-later

from odoo import fields, models


class AccountMove(models.Model):
    _inherit = "account.move"

    consumption_graph_svg = fields.Text()
    show_svg_field = fields.Boolean(string="Show SVG Code Field", default=False)

    def action_toggle_svg_visibility(self):
        for record in self:
            record.show_svg_field = not record.show_svg_field
