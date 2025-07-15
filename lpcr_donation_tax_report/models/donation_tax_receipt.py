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
        domain=[],
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
        res_partner_model = self.env["res.partner"]
        new_vals_list = []
        for vals in vals_list:
            partner_id = res_partner_model.browse(vals.get("partner_id"))
            if not partner_id.is_address_valid:
                raise UserError(
                    _(
                        "Le reçu fiscal n'a pas pu être émis car il manque des "
                        "informations.\n"
                        "Le nom, le prénom et l'adresse postale (rue et numéro, "
                        "code postal, ville, pays) des personnes doivent "
                        "être définis.\n"
                        "Le nom, le numéro SIRET et l'adresse postale (rue et "
                        "numéro, code postal, ville, pays) des sociétés "
                        "doivent être définis."
                    )
                )
            address_at_creation = {
                "donor_name": partner_id.name,
                "street": partner_id.street,
                "street2": partner_id.street2,
                "city": partner_id.city,
                "state_id": partner_id.state_id.id,
                "state_name": partner_id.state_id.name,
                "zip": partner_id.zip,
                "country_id": partner_id.country_id.id,
                "country_name": partner_id.country_id.name,
            }
            if partner_id.is_company:
                address_at_creation["siret"] = partner_id.siret
            new_vals = vals.copy()
            new_vals.update(address_at_creation)
            new_vals_list.append(new_vals)
        return super().create(new_vals_list)

    @api.model
    def update_tax_receipt_annual_dict(
        self, tax_receipt_annual_dict, start_date, end_date, company
    ):
        res = super().update_tax_receipt_annual_dict(
            tax_receipt_annual_dict, start_date, end_date, company
        )
        if not self.env.context.get("donation_tax_receipt_include_incomplete_partners"):
            for partner in list(tax_receipt_annual_dict.keys()):
                if not partner.is_address_valid:
                    del tax_receipt_annual_dict[partner]
        return res
