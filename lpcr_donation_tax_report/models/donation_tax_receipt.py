# SPDX-FileCopyrightText: 2025 Coop IT Easy SC
#
# SPDX-License-Identifier: AGPL-3.0-or-later

from odoo import _, api, fields, models
from odoo.exceptions import UserError


class DonationTaxReceipt(models.Model):
    _inherit = "donation.tax.receipt"

    # Remove the domain restriction that partner can't have parent
    # because we want individuals not just their companies
    partner_id = fields.Many2one(
        "res.partner",
        string="Donor",
        required=True,
        ondelete="restrict",
        index=True,
        tracking=True,
    )

    email = fields.Char(related="partner_id.email")
    donor_name = fields.Char(
        readonly=True,
    )
    street = fields.Char(
        readonly=True,
    )
    street2 = fields.Char(
        readonly=True,
    )
    city = fields.Char(
        readonly=True,
    )
    state_id = fields.Many2one(
        "res.country.state",
        readonly=True,
    )
    state_name = fields.Char(
        readonly=True,
    )
    zip = fields.Char(
        readonly=True,
    )
    country_id = fields.Many2one(
        "res.country",
        readonly=True,
    )
    country_name = fields.Char(
        readonly=True,
    )
    siret = fields.Char(
        readonly=True,
    )

    @api.model_create_multi
    def create(self, vals_list):
        result_list = super().create(vals_list)
        for result in result_list:
            is_partner_address_valid = bool(
                result.partner_id.street
                and result.partner_id.city
                and result.partner_id.zip
                and result.partner_id.country_id
                and (result.partner_id.siret or not result.partner_id.is_company)
            )
            if not is_partner_address_valid:
                raise UserError(
                    _(
                        "Le reçu discal n'a pas pu être émis car "
                        "il manque des informations. \n"
                        "Le nom, le prénom et l'adresse postale (rue et numéro"
                        ", code postale, ville, pays) des personnes doivent "
                        "être définis. \n"
                        "Le nom, le numéro SIRET et l'adresse postale (rue et "
                        "numéro, code postale, ville, pays) des sociétés "
                        "doivent être définis."
                    )
                )
            address_at_creation = {
                "donor_name": result.partner_id.name,
                "street": result.partner_id.street,
                "street2": result.partner_id.street2,
                "city": result.partner_id.city,
                "state_id": result.partner_id.state_id,
                "state_name": result.partner_id.state_id.name,
                "zip": result.partner_id.zip,
                "country_id": result.partner_id.country_id,
                "country_name": result.partner_id.country_id.name,
            }
            if result.partner_id.is_company:
                address_at_creation["siret"] = result.partner_id.siret
            result.update(address_at_creation)
        return result_list
