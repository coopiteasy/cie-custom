# SPDX-FileCopyrightText: 2025 Coop IT Easy SC
#
# SPDX-License-Identifier: AGPL-3.0-or-later

from odoo import fields, models


class ProductProduct(models.Model):
    _inherit = "product.product"

    short_name = fields.Char(
        "Short name",
        related="product_tmpl_id.short_name",
        readonly=False,
    )
