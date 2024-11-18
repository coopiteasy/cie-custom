# SPDX-FileCopyrightText: 2024 Coop IT Easy SC
#
# SPDX-License-Identifier: AGPL-3.0-or-later

from odoo import api, fields, models


class ProductProduct(models.Model):
    _inherit = "product.product"

    lst_price_taxes_included = fields.Float(
        "Sales Price (Taxes Included)",
        compute="_compute_lst_price_taxes_included",
        digits="Product Price",
    )

    @api.depends("lst_price", "company_id.currency_id")
    def _compute_lst_price_taxes_included(self):
        for rec in self:
            company = rec.company_id or self.env.company
            if not rec.taxes_id:
                rec.lst_price_taxes_included = rec.lst_price
            rec.lst_price_taxes_included = rec.taxes_id.compute_all(
                rec.lst_price, company.currency_id, 1, product=rec
            )["total_included"]
