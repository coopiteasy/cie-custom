from odoo import fields, models


class ResPartner(models.Model):
    _name = "res.partner"
    _inherit = ["res.partner", "data.historization.mixin"]

    historization_ids = fields.One2many(
        comodel_name="data.historization.res.partner", inverse_name="partner_id"
    )

    _historization_fields = [
        "name",
        "active",
        "main_income_source_household",
        "main_income_source_member",
        "household_situation_id",
        "job_position_id",
        "gender",
        "city",
        "monthly_savings_per_person",
        "daily_savings_per_person",
        # # A tester
        "total_income",
        "total_expenditure",
    ]

    _raise_historization_fields = ["social_budget_move_ids"]
