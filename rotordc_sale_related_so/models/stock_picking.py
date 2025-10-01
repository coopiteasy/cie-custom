# SPDX-FileCopyrightText: 2023 Coop IT Easy SC
#
# SPDX-License-Identifier: AGPL-3.0-or-later

from odoo import fields, models


class StockPicking(models.Model):
    _inherit = "stock.picking"

    related_so_ids = fields.Many2many(
        string="Linked Sale Orders",
        related="sale_id.related_so_ids",
    )
