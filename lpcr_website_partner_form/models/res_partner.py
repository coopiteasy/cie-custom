# SPDX-FileCopyrightText: 2025 Coop IT Easy SC
#
# SPDX-License-Identifier: AGPL-3.0-or-later

from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    customer_type_id = fields.Many2one(
        string="Customer Type",
        comodel_name="res.partner.customer.type",
    )
    acquisition_medium_id = fields.Many2one(
        string="Acquisition Medium",
        comodel_name="res.partner.acquisition.medium",
    )
