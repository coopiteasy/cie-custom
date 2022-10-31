# SPDX-FileCopyrightText: 2022 Coop IT Easy SC
#
# SPDX-License-Identifier: AGPL-3.0-or-later

from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    # All below fields just have copy=True added to them.
    volume = fields.Float(copy=True)
    weight = fields.Float(copy=True)
    # FIXME: We should probably do variant_seller_ids as well. However, when
    # setting copy=True on both seller_ids and variant_seller_ids, copying
    # breaks due to a strange TypeError (NoneType object is not subscriptable).
    # Because the inverse name is identical (product_tmpl_id) for both fields,
    # it is probably _fine_ as-is.
    seller_ids = fields.One2many(
        "product.supplierinfo",
        "product_tmpl_id",
        copy=True,
    )
    default_code = fields.Char(copy=True)
    hs_code_id = fields.Many2one(
        "hs.code",
        copy=True,
    )
    origin_country_id = fields.Many2one(
        "res.country",
        copy=True,
    )
