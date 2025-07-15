# SPDX-FileCopyrightText: 2025 Coop IT Easy SC
#
# SPDX-License-Identifier: AGPL-3.0-or-later

from odoo import fields, models


class DonationDonation(models.Model):
    _inherit = "donation.donation"

    is_donor_address_valid = fields.Boolean(
        string="Complete info", related="partner_id.is_address_valid"
    )

    # commercial_partner_id is the parent company of partner, and is used as
    # the partner of the donation, but we want the actual partner here not his
    # company
    commercial_partner_id = fields.Many2one(
        related="partner_id",
    )
