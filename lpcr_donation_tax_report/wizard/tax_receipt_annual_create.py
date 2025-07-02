# SPDX-FileCopyrightText: 2025 Coop IT Easy SC
#
# SPDX-License-Identifier: AGPL-3.0-or-later

import logging

from odoo import _, models
from odoo.exceptions import UserError

logger = logging.getLogger(__name__)


class TaxReceiptAnnualCreate(models.TransientModel):
    _inherit = "tax.receipt.annual.create"

    def generate_annual_receipts(self):

        self.ensure_one()
        logger.info(
            "Start to generate annual fiscal receipts from %s to %s",
            self.start_date,
            self.end_date,
        )

        tax_receipt_annual_dict = {}
        self.env["donation.tax.receipt"].update_tax_receipt_annual_dict(
            tax_receipt_annual_dict, self.start_date, self.end_date, self.company_id
        )
        filtered_tax_receipt_annual_dict = {
            partner: partner_dict
            for (partner, partner_dict) in tax_receipt_annual_dict.items()
            if partner.is_address_valid
        }
        is_some_partner_incomplete = bool(
            len(tax_receipt_annual_dict) - len(filtered_tax_receipt_annual_dict)
        )

        dtro = self.env["donation.tax.receipt"]
        existing_annual_receipts = dtro.search(
            [
                ("donation_date", "<=", self.end_date),
                ("donation_date", ">=", self.start_date),
                ("company_id", "=", self.company_id.id),
                ("type", "=", "annual"),
            ]
        )
        existing_annual_receipts_dict = {}
        for receipt in existing_annual_receipts:
            existing_annual_receipts_dict[receipt.partner_id] = receipt

        tax_receipt_ids = []
        for partner, partner_dict in filtered_tax_receipt_annual_dict.items():
            vals = self._prepare_annual_tax_receipt(partner, partner_dict)
            tax_receipt = dtro.create(vals)
            tax_receipt_ids.append(tax_receipt.id)
            logger.info("Tax receipt %s generated", tax_receipt.number)
        if not tax_receipt_ids:
            raise UserError(
                _(
                    "No annual tax receipt to generate \n"
                    "If it is expected for new tax receipts to be generated, "
                    "this could mean the donors' informations (postal address "
                    "or SIRET number) are incomplete"
                )
            )

        logger.info("%d annual fiscal receipts generated", len(tax_receipt_ids))
        if is_some_partner_incomplete:
            action = {
                "type": "ir.actions.client",
                "tag": "display_notification",
                "params": {
                    "title": _("Attention"),
                    "type": "warning",
                    "sticky": True,
                    "message": _(
                        "Un ou plusieurs reçus fiscaux n’ont pas été émis car "
                        "l'adresse postale ou le numéro SIRET sont manquants."
                        "Veuillez compléter les informations des contacts"
                        " dont les données sont incomplètes."
                    ),
                },
            }
        else:
            action = (
                self.env.ref("donation_base.donation_tax_receipt_action")
                .sudo()
                .read([])[0]
            )
            action["domain"] = [("id", "in", tax_receipt_ids)]

        return action
