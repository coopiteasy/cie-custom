# SPDX-FileCopyrightText: 2024 Coop IT Easy SC
#
# SPDX-License-Identifier: AGPL-3.0-or-later

from odoo import fields, models


class StockMoveLine(models.Model):
    _inherit = "stock.move.line"
    _order = "product_category_name,product_default_code"

    product_default_code = fields.Char(related="product_id.default_code", store=True)
