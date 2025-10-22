# SPDX-FileCopyrightText: 2025 Coop IT Easy SC
#
# SPDX-License-Identifier: AGPL-3.0-or-later

from odoo import models


class PricelistItem(models.Model):
    _name = "product.pricelist.item"
    _inherit = "product.pricelist.item"

    def get_price_per_weight(self, product):
        if product.weight == 0:
            return False
        return (
            product.with_context(pricelist=self.pricelist_id.id)._get_contextual_price()
            / product.weight
        )
