# SPDX-FileCopyrightText: 2026 Coop IT Easy SC
#
# SPDX-License-Identifier: AGPL-3.0-or-later

from odoo import fields, models


class PartnerSocialResidencePermitTitle(models.Model):
    _name = "partner.social.residence.permit.title"
    _description = "Social Residence Permit Title"
    _order = "name"

    name = fields.Char(required=True, translate=True)
    active = fields.Boolean(default=True)

    _sql_constraints = [
        ("name_uniq", "unique(name)", "Name already exists!"),
    ]
