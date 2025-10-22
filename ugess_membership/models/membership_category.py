# Copyright 2023 Akretion (https://www.akretion.com).
# @author Pierrick Brun <pierrick.brun@akretion.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class MembershipMembershipCategory(models.Model):
    _inherit = "membership.membership_category"

    ugess_type = fields.Selection(
        selection=[
            ("beneficiary", "Beneficiary"),
            ("solidary", "Solidary"),
        ]
    )
