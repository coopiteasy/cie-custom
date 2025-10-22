from odoo import fields, models


class SocialBudgetMoveCategory(models.Model):
    _name = "social.budget.move.category"
    _description = "Social Budget Move Categories"

    name = fields.Char(
        string="Category",
        required=True,
    )
    type = fields.Selection(
        selection=[("income", "Income"), ("expenditure", "Expenditure")],
        default="income",
        string="Type",
        required=True,
    )
