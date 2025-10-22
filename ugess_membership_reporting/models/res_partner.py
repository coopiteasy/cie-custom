# Copyright 2023 Akretion (https://www.akretion.com).
# @author Pierrick Brun <pierrick.brun@akretion.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    total_income = fields.Monetary(store=True)
    total_expenditure = fields.Monetary(store=True)

    number_of_persons_in_household = fields.Integer(store=True)
    number_of_babies_in_household = fields.Integer(store=True)
    number_of_children_in_household = fields.Integer(store=True)
    number_of_adult_in_household = fields.Integer(store=True)

    # Not necessary but make the rel/column names explicit
    membership_category_ids = fields.Many2many(
        relation="membership_membership_category_res_partner_rel",
        column1="res_partner_id",
        column2="membership_membership_category_id",
    )
