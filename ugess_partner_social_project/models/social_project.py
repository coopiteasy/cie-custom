from odoo import fields, models


class SocialProject(models.Model):
    _name = "social.project"
    _description = "Social Project"

    type_id = fields.Many2one(
        comodel_name="social.project.type", string="Type", required=True
    )
    realization_rate = fields.Selection(
        selection=[
            ("0", "0"),
            ("25", "25"),
            ("50", "50"),
            ("75", "75"),
            ("100", "100"),
        ],
    )
    partner_id = fields.Many2one(comodel_name="res.partner")
    start_date = fields.Date(default=fields.Datetime.now)
    end_date = fields.Date()

    name = fields.Char(
        string="Description",
        required=True,
    )
    comment = fields.Text()
