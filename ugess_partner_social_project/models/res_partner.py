from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    social_project_ids = fields.One2many(
        comodel_name="social.project",
        inverse_name="partner_id",
        string="Social Project",
    )
