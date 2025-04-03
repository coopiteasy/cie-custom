# SPDX-FileCopyrightText: 2025 Coop IT Easy SC
#
# SPDX-License-Identifier: AGPL-3.0-or-later

from odoo import fields, models


class ResPartnerAcquisitionMedium(models.Model):
    _name = "res.partner.acquisition.medium"
    _description = "How partner get acquired"

    name = fields.Char(required=True)
    partner_ids = fields.One2many(
        string="Partners",
        comodel_name="res.partner",
        inverse_name="acquisition_medium_id",
    )
