from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    entry_interview_done = fields.Boolean()
    exit_interview_done = fields.Boolean()

    referent_id = fields.Many2one(
        comodel_name="res.partner",
        string="Referent",
    )
