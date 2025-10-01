# SPDX-FileCopyrightText: 2024 Coop IT Easy SC
#
# SPDX-License-Identifier: AGPL-3.0-or-later

from odoo import api, fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    list_price_taxes_included = fields.Float(
        "Sales Price (Taxes Included)",
        compute="_compute_list_price_taxes_included",
        digits="Product Price",
    )

    @api.depends("list_price", "company_id.currency_id")
    def _compute_list_price_taxes_included(self):
        for rec in self:
            company = rec.company_id or self.env.company
            if not rec.taxes_id:
                rec.list_price_taxes_included = rec.list_price
            rec.list_price_taxes_included = rec.taxes_id.compute_all(
                rec.list_price, company.currency_id, 1, product=rec
            )["total_included"]
