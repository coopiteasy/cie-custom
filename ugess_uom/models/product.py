# Copyright 2023 Akretion (https://www.akretion.com).
# @author Pierrick Brun <pierrick.brun@akretion.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, models


class ProductProduct(models.Model):
    _inherit = "product.template"

    @api.depends("uom_id", "weight")
    def _compute_weight(self):
        res = super()._compute_weight()
        self._set_product_weight_uom_kg()
        return res

    def _set_weight(self):
        res = super()._set_weight()
        self._set_product_weight_uom_kg()
        return res

    def _set_product_weight_uom_kg(self):
        for record in self:
            if record.uom_id == self.env.ref("uom.product_uom_kgm"):
                # Si le produit est vendu au kg ça n'a pas de sens
                # Que le poids ne soit pas 1
                record.weight = 1
