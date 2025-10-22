# Copyright 2023 Akretion (https://www.akretion.com).
# @author Pierrick Brun <pierrick.brun@akretion.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models

from odoo.addons.membership.report.report_membership import STATE


class ReportMembership(models.Model):
    """Membership Analysis"""

    _inherit = "report.membership"

    membership_category_ids = fields.Many2many(
        "membership.membership_category",
        relation="membership_membership_category_res_partner_rel",
        column1="res_partner_id",
        column2="membership_membership_category_id",
        readonly=True,
    )
    expenditure_ceiling = fields.Monetary(readonly=True, group_operator="avg")
    expenditure_ceiling_period = fields.Selection(
        selection=[
            ("week", "Week"),
            ("month", "Month"),
            ("year", "Year"),
        ],
        readonly=True,
    )
    social_project_type_id = fields.Many2one("social.project.type", readonly=True)
    social_project_realization_rate = fields.Char(readonly=True)
    currency_id = fields.Many2one("res.currency", readonly=True)
    social_worker_id = fields.Many2one("res.partner", readonly=True)
    social_organization_id = fields.Many2one("res.partner", readonly=True)
    district_id = fields.Many2one("res.district", readonly=True)
    age_group = fields.Char(readonly=True)
    gender = fields.Char(readonly=True)
    total_income = fields.Monetary(readonly=True, group_operator="avg")
    total_expenditure = fields.Monetary(readonly=True, group_operator="avg")
    number_of_persons_in_household = fields.Integer(readonly=True)
    number_of_babies_in_household = fields.Integer(readonly=True)
    number_of_children_in_household = fields.Integer(readonly=True)
    number_of_adults_in_household = fields.Integer(readonly=True)
    number_of_males_in_household = fields.Integer(readonly=True)
    number_of_females_in_household = fields.Integer(readonly=True)
    number_of_other_genders_in_household = fields.Integer(readonly=True)
    number_of_unknown_genders_in_household = fields.Integer(readonly=True)
    monthly_savings_per_person = fields.Monetary(readonly=True, group_operator="avg")
    daily_savings_per_person = fields.Monetary(readonly=True, group_operator="avg")
    main_income_source_household = fields.Many2one(
        "social.budget.move.category", readonly=True
    )
    membership_line_state = fields.Selection(STATE, readonly=True)
    membership_line_start_date = fields.Date(readonly=True)

    def _select(self):
        res = super()._select()
        res += """
        , MAX(ml.expenditure_ceiling) AS expenditure_ceiling
        , ml.expenditure_ceiling_period AS expenditure_ceiling_period
        , am.currency_id AS currency_id
        , p.referent_id AS social_worker_id
        , sw.parent_id AS social_organization_id
        , sp.type_id AS social_project_type_id
        , sp.realization_rate AS social_project_realization_rate
        , p.district_id AS district_id
        , AVG(p.total_income) AS total_income
        , AVG(p.total_expenditure) AS total_expenditure
        , hm.age_group AS age_group
        , hm.gender AS gender
        , SUM(p.number_of_persons_in_household) AS number_of_persons_in_household
        , SUM(p.number_of_babies_in_household) AS number_of_babies_in_household
        , SUM(p.number_of_children_in_household) AS number_of_children_in_household
        , SUM(p.number_of_adult_in_household) AS number_of_adults_in_household
        , SUM(p.number_of_males_in_household) AS number_of_males_in_household
        , SUM(p.number_of_females_in_household) AS number_of_females_in_household
        , SUM(p.number_of_other_genders_in_household)
        AS number_of_other_genders_in_household
        , SUM(p.number_of_unknown_genders_in_household)
        AS number_of_unknown_genders_in_household
        , MAX(p.monthly_savings_per_person) AS monthly_savings_per_person
        , MAX(p.daily_savings_per_person) AS daily_savings_per_person
        , p.main_income_source_household AS main_income_source_household
        , ml.state AS membership_line_state
        , ml.date_from AS membership_line_start_date
        """
        return res

    def _from(self):
        res = super()._from()
        res += """
            LEFT JOIN res_partner sw ON (p.referent_id = sw.id)
            LEFT JOIN social_project sp ON (ml.social_project_id = sp.id)
            LEFT JOIN household_member hm ON (p.linked_household_member_id = hm.id)
        """
        return res

    def _group_by(self):
        res = super()._group_by()
        res += """
            , am.currency_id
            , sw.parent_id
            , sp.type_id
            , sp.realization_rate
            , ml.state
            , ml.date_from
            , ml.expenditure_ceiling_period
            , hm.age_group
            , hm.gender
        """
        return res
