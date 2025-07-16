# SPDX-FileCopyrightText: 2025 Coop IT Easy SC
#
# SPDX-License-Identifier: AGPL-3.0-or-later

from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    is_address_valid = fields.Boolean(
        string="Complete Info",
        store=True,
        compute="_compute_address_valid",
    )

    @api.depends(
        "name",
        "street",
        "city",
        "zip",
        "country_id",
        "siret",
        "is_company",
    )
    def _compute_address_valid(self):
        for record in self:
            record.is_address_valid = bool(
                record.name
                and record.street
                and record.city
                and record.zip
                and record.country_id
                and (record.siret or not record.is_company)
            )
