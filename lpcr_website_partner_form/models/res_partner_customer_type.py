# SPDX-FileCopyrightText: 2025 Coop IT Easy SC
#
# SPDX-License-Identifier: AGPL-3.0-or-later

from odoo import fields, models


class ResPartnerCustomerType(models.Model):
    _name = "res.partner.customer.type"
    _description = "Customer Type for Partners"

    name = fields.Char(required=True)
    partner_ids = fields.One2many(
        string="Partners",
        comodel_name="res.partner",
        inverse_name="customer_type_id",
    )
