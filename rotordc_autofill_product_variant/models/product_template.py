# Copyright 2022 Coop IT Easy SCRL fs
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    def _prepare_variant_values(self, combination):
        """
        See explanation in the same method in the product_dimension module.
        """
        res = super()._prepare_variant_values(combination)
        if self.default_code:
            res.update({"default_code": self.default_code})
        if self.weight:
            res.update({"weight": self.weight})
        # product_dimension attributes are automatically copied by the
        # product_dimension module.
        return res
