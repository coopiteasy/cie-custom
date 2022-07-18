# SPDX-FileCopyrightText: 2022 Coop IT Easy SC
#
# SPDX-License-Identifier: AGPL-3.0-or-later

from odoo import fields, models


class ProductStorageLocation(models.Model):
    _name = "product.storage_location"
    _description = "Storage Location"

    name = fields.Char(string="Name", required=True)

    _sql_constraints = [
        (
            "name_unique",
            "UNIQUE (name)",
            "Location name must be unique",
        )
    ]
