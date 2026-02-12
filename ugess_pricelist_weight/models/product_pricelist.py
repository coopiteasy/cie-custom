# SPDX-FileCopyrightText: 2025 Coop IT Easy SC
#
# SPDX-License-Identifier: AGPL-3.0-or-later

from odoo import fields, models


class ProductPricelist(models.Model):
    _inherit = "product.pricelist"

    def _get_current_applicable_rules(self, products, **kwargs):
        date = fields.Datetime.now()
        rules = self._get_applicable_rules(products, date, **kwargs)
        return rules
