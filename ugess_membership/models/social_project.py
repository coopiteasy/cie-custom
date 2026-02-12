# SPDX-FileCopyrightText: 2022 Coop IT Easy SC
#
# SPDX-License-Identifier: AGPL-3.0-or-later

from odoo import fields, models


class SocialProject(models.Model):
    _inherit = "social.project"

    membership_line_ids = fields.One2many(
        comodel_name="membership.membership_line",
        inverse_name="social_project_id",
        string="Membership Lines",
    )
