# Copyright 2022 Akretion (https://www.akretion.com).
# @author Pierrick Brun <pierrick.brun@akretion.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    supplier_id = fields.Many2one("res.partner", domain="[('is_company', '=', True)]")
    supply_source_id = fields.Many2one(
        "supply.source",
    )
