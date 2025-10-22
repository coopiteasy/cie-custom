from odoo import fields, models


class SocialProjectType(models.Model):
    _name = "social.project.type"
    _description = "Social Project Type"

    name = fields.Char(
        string="Type",
        required=True,
    )
