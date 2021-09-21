# Copyright 2020 Coop IT Easy SCRL fs
#   Robin Keunen <robin@coopiteasy.be>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class HRDepartment(models.Model):
    _inherit = "hr.department"

    bob_code = fields.Char(string="Bob Code")
