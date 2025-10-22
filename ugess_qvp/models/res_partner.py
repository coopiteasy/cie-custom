from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    political_quarter = fields.Boolean()
