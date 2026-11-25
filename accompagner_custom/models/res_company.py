# SPDX-FileCopyrightText: 2026 Coop IT Easy SC
#
# SPDX-License-Identifier: AGPL-3.0-or-later

from odoo import fields, models


class ResCompany(models.Model):
    _inherit = "res.company"

    partner_properties_definition_social_beneficiary = fields.PropertiesDefinition(
        "social_beneficiary"
    )
    partner_properties_definition_social_volunteer = fields.PropertiesDefinition(
        "social_volunteer"
    )
    partner_properties_definition_social_partner = fields.PropertiesDefinition(
        "social_partner"
    )
    partner_properties_definition_social_benefactor = fields.PropertiesDefinition(
        "social_benefactor"
    )
