from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    entry_interview_done = fields.Boolean(string="Entry Interview Done")
    exit_interview_done = fields.Boolean(string="Exit Interview Done")

    referent_id = fields.Many2one(
        comodel_name="res.partner",
        string="Referent",
    )
