# SPDX-FileCopyrightText: 2025 Coop IT Easy SC
#
# SPDX-License-Identifier: AGPL-3.0-or-later

from odoo import _, api, fields, models
from odoo.exceptions import UserError


class ProductPrintCategory(models.Model):
    _name = "product.print.category"
    _inherit = "product.print.category"

    is_multipricetag = fields.Boolean(
        string="Multi-price",
        default=True,
    )

    price_lists_ids = fields.Many2many(
        string="Pricelists",
        comodel_name="product.pricelist",
        check_company=True,
    )

    @api.constrains("company_id")
    def _check_price_lists_company(self):
        for record in self:
            if record.price_lists_ids and record.company_id:
                for pricelist in record.price_lists_ids:
                    if (
                        pricelist.company_id != record.company_id
                        and pricelist.company_id is not False
                    ):
                        raise UserError(
                            _(
                                "All price lists must belong to the same company"
                                " as the product print category. \n"
                                "Please check the price lists associated with"
                                " this category and remove those belonging to"
                                " the wrong company."
                            )
                        )
