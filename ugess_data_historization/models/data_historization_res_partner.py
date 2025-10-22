from odoo import fields, models


class DataHistorizationResPartner(models.Model):
    _name = "data.historization.res.partner"
    _description = "Historization of res.partner"

    partner_id = fields.Many2one(comodel_name="res.partner")

    name = fields.Char()

    active = fields.Boolean()

    main_income_source_household = fields.Many2one(
        comodel_name="social.budget.move.category",
        string="Main Income Source of Household",
        groups="ugess_partner_household.group_ugess_partner_household_user",
    )
    main_income_source_member = fields.Many2one(
        comodel_name="social.budget.move.category",
        string="Main Income Source of Member",
        groups="ugess_partner_household.group_ugess_partner_household_user",
    )
    household_situation_id = fields.Many2one(
        comodel_name="household.situation",
        string="Household Situation",
        groups="ugess_partner_household.group_ugess_partner_household_user",
    )

    job_position_id = fields.Many2one(
        comodel_name="res.partner.job_position",
        string="Categorized job position",
        groups="ugess_partner_household.group_ugess_partner_household_user",
    )

    gender = fields.Selection(
        selection=lambda self: self.env["res.partner"]._fields["gender"].selection,
        groups="ugess_partner_household.group_ugess_partner_household_user",
    )

    city = fields.Char()

    monthly_savings_per_person = fields.Float(
        groups="ugess_partner_revenue.group_ugess_partner_revenue_user"
    )

    daily_savings_per_person = fields.Float(
        groups="ugess_partner_revenue.group_ugess_partner_revenue_user"
    )

    total_income = fields.Float(
        groups="ugess_partner_revenue.group_ugess_partner_revenue_user"
    )

    total_expenditure = fields.Float(
        groups="ugess_partner_revenue.group_ugess_partner_revenue_user"
    )
