from odoo import fields, models


class DataHistorizationHouseholdMember(models.Model):
    _name = "data.historization.household.member"
    _description = "Historization of household.member"

    household_member_id = fields.Many2one(comodel_name="household.member")

    name = fields.Char()

    is_active_member = fields.Boolean()

    gender = fields.Selection(
        selection=lambda self: self.env["household.member"]._fields["gender"].selection
    )

    job_position_id = fields.Many2one(
        comodel_name="res.partner.job_position", string="Categorized job position"
    )

    main_income_source = fields.Many2one(
        comodel_name="social.budget.move.category",
    )
