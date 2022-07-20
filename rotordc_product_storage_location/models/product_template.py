# SPDX-FileCopyrightText: 2022 Coop IT Easy SC
#
# SPDX-License-Identifier: AGPL-3.0-or-later

from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    storage_location = fields.Many2one(
        comodel_name="product.storage_location",
        string="Storage Location",
        ondelete="set null",
    )
