# Copyright 2020 Coop IT Easy SCRL fs
#   Robin Keunen <robin@coopiteasy.be>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class ProVeloFinancing(models.Model):
    _name = "pv.financing"
    _description = "Pro Velo Financing"

    name = fields.Char()
    active = fields.Boolean(default=True)
    bob_code = fields.Char(string="Bob Code")
