# Copyright 2023 Coop IT Easy SC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class Contract(models.Model):
    _inherit = "contract.contract"
    support_line_ids = fields.One2many(
        comodel_name="contract.line",
        related="contract_line_ids",
    )  # fixme can't modify the line because it's a related fields => need to be able to edit project _id


class ContractLine(models.Model):
    _inherit = "contract.line"

    project_id = fields.Many2one(
        string="Project",
        comodel_name="project.project",
    )
    is_support_line = fields.Boolean(
        related="product_id.is_support_product",
    )
    nb_included_hours = fields.Float(related="product_id.nb_included_hours")
