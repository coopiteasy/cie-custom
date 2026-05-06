# SPDX-FileCopyrightText: 2026 Coop IT Easy SC
#
# SPDX-License-Identifier: AGPL-3.0-or-later

import base64

from odoo import api, fields, models


class AccountMove(models.Model):
    _inherit = "account.move"

    consumption_graph_image = fields.Binary(
        "Consumption Graph",
    )
    # this field is only to be able to get and set the data as text (by api)
    consumption_graph_svg = fields.Text(
        compute="_compute_consumption_graph_svg",
        inverse="_inverse_consumption_graph_svg",
    )

    @api.depends("consumption_graph_image")
    def _compute_consumption_graph_svg(self):
        # if the consumption graph is defined, use its content as text.
        # otherwise, return an empty string.
        for rec in self:
            image_data = rec.consumption_graph_image
            if not image_data:
                rec.consumption_graph_svg = ""
            else:
                rec.consumption_graph_svg = base64.b64decode(image_data).decode("utf-8")

    def _inverse_consumption_graph_svg(self):
        for rec in self:
            svg_text = rec.consumption_graph_svg
            if not svg_text:
                rec.consumption_graph_image = False
            else:
                rec.consumption_graph_image = base64.b64encode(svg_text.encode("utf-8"))
