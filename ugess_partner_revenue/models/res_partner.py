from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    social_budget_move_ids = fields.One2many(
        comodel_name="social.budget.move",
        inverse_name="partner_id",
        string="Social Budget Moves",
    )

    total_income = fields.Monetary(
        compute="_compute_total_amount",
        store=False,
    )
    total_expenditure = fields.Monetary(
        compute="_compute_total_amount",
        store=False,
    )

    @api.depends(
        "social_budget_move_ids",
        "social_budget_move_ids.income",
        "social_budget_move_ids.expenditure",
        "social_budget_move_ids.type",
    )
    def _compute_total_amount(self):
        for rec in self:
            moves = self.env["social.budget.move"].search([("partner_id", "=", rec.id)])
            rec.total_income = sum(
                moves.filtered(lambda m: m.type == "income").mapped("income")
            )
            rec.total_expenditure = sum(
                moves.filtered(lambda m: m.type == "expenditure").mapped("expenditure")
            )

    monthly_savings_per_person = fields.Monetary()
    daily_savings_per_person = fields.Monetary()
