from odoo import fields, models


class SocialBudgetMove(models.Model):
    _name = "social.budget.move"
    _description = "Social Budget Move"

    category_id = fields.Many2one(
        comodel_name="social.budget.move.category", string="Category", required=True
    )
    expenditure = fields.Monetary(
        string="Debit",
    )
    income = fields.Monetary(
        string="Credit",
    )
    currency_id = fields.Many2one(
        comodel_name="res.currency", related="company_id.currency_id", readonly=True
    )
    company_id = fields.Many2one(
        comodel_name="res.company",
        default=lambda self: self.env.company,
        readonly=True,
        string="Company",
    )

    type = fields.Selection(
        related="category_id.type",
        string="Type",
    )
    partner_id = fields.Many2one(comodel_name="res.partner", string="Contact")
