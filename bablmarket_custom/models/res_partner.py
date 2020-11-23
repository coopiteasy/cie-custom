from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    email_formatted = fields.Char(store=True)
