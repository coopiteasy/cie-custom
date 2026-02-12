from odoo import fields, models


class HouseholdSituation(models.Model):
    _name = "household.situation"
    _description = "Household Situation"

    name = fields.Char(
        required=True,
    )
