# SPDX-FileCopyrightText: 2025 Coop IT Easy SC
#
# SPDX-License-Identifier: AGPL-3.0-or-later

from odoo import fields, models


class DonationDonation(models.Model):
    _inherit = "donation.donation"

    is_donor_address_valid = fields.Boolean(
        string="Complete info", related="partner_id.is_address_valid"
    )
