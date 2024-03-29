# Copyright 2020 Coop IT Easy SCRL fs
#   Robin Keunen <robin@coopiteasy.be>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class ResourceActivityType(models.Model):
    _inherit = "resource.activity.type"

    project_id = fields.Many2one(
        comodel_name="pv.project", string="Project", required=False
    )
