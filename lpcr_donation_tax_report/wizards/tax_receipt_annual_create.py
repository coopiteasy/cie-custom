# SPDX-FileCopyrightText: 2025 Coop IT Easy SC
#
# SPDX-License-Identifier: AGPL-3.0-or-later

import logging

from odoo import api, fields, models

logger = logging.getLogger(__name__)


class TaxReceiptAnnualCreate(models.TransientModel):
    _inherit = "tax.receipt.annual.create"

    valid_tax_receipts_count = fields.Integer(compute="_compute_tax_receipts_count")
    invalid_tax_receipts_count = fields.Integer(compute="_compute_tax_receipts_count")

    @api.depends("start_date", "end_date", "company_id")
    def _compute_tax_receipts_count(self):
        tax_receipt_annual_dict = {}
        self.env["donation.tax.receipt"].with_context(
            donation_tax_receipt_include_incomplete_partners=True
        ).update_tax_receipt_annual_dict(
            tax_receipt_annual_dict, self.start_date, self.end_date, self.company_id
        )
        filtered_tax_receipt_annual_dict = {
            partner: partner_dict
            for (partner, partner_dict) in tax_receipt_annual_dict.items()
            if partner.is_address_valid
        }
        self.valid_tax_receipts_count = len(filtered_tax_receipt_annual_dict)
        self.invalid_tax_receipts_count = len(tax_receipt_annual_dict) - len(
            filtered_tax_receipt_annual_dict
        )
