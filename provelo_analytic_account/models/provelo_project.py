# Copyright 2020 Coop IT Easy SCRL fs
#   Robin Keunen <robin@coopiteasy.be>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class ProVeloProject(models.Model):
    _name = "pv.project"
    _description = "Pro Velo Project"

    name = fields.Char()
    active = fields.Boolean(default=True)
    bob_code = fields.Char(string="Bob Code")
    location_id = fields.Many2one(
        comodel_name="resource.location", string="Location", required=True
    )
    department_id = fields.Many2one(
        comodel_name="hr.department", string="Department", required="True"
    )
    allowed_financing_ids = fields.Many2many(
        comodel_name="pv.financing",
        string="Allowed Financing",
        help="Restricts allowed financing for this project on the invoice.",
    )
