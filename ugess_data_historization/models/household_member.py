from odoo import fields, models


class HouseholdMember(models.Model):
    _name = "household.member"
    _inherit = ["household.member", "data.historization.mixin"]

    historization_ids = fields.One2many(
        comodel_name="data.historization.household.member",
        inverse_name="household_member_id",
    )

    _historization_fields = [
        "name",
        "is_active_member",
        "gender",
        "job_position_id",
        "main_income_source",
    ]
