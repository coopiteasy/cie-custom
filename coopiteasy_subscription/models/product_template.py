# Copyright 2023 Coop IT Easy SC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    is_support_product = fields.Boolean()
    nb_included_hours = fields.Float(
        string="Number of included hours",
        default=0,
    )
