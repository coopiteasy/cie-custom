# SPDX-FileCopyrightText: 2022 Coop IT Easy SC
#
# SPDX-License-Identifier: AGPL-3.0-or-later

from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    # FIXME: Maybe move this to another module.
    membership_pricelist_id = fields.Many2one(
        comodel_name="product.pricelist",
        string="Membership Pricelist",
    )
