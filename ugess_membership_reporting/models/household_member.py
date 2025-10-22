# Copyright 2023 Akretion (https://www.akretion.com).
# @author Pierrick Brun <pierrick.brun@akretion.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).


from odoo import fields, models


class HouseholdMember(models.Model):
    _inherit = "household.member"

    age_group = fields.Selection(store=True)
