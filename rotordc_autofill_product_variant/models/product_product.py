# Copyright 2022 Coop IT Easy SCRL fs
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).


from itertools import groupby

from odoo import api, models


class ProductProduct(models.Model):
    _inherit = "product.product"

    @api.model_create_multi
    def create(self, vals_list):
        """Copy some field from the product template to the new variant"""
        # Be mindful that this method is also entered during the creation of a
        # product_template.product_variant_id.

        # Enter this loop once for every product.template. `group_vals` is an
        # iterator of vals for each product that has the same template.
        for tmpl_id, group_vals in groupby(
            vals_list, lambda elem: elem.get("product_tmpl_id", None)
        ):
            if not tmpl_id:
                continue
            product_tmpl_id = self.env["product.template"].browse(tmpl_id)
            for vals in group_vals:
                if "default_code" not in vals:
                    vals["default_code"] = product_tmpl_id.default_code
                if "weight_uom_id" not in vals:
                    vals["weight_uom_id"] = product_tmpl_id.weight_uom_id.id
                if "weight" not in vals:
                    vals["weight"] = product_tmpl_id.weight
                if "dimensional_uom_id" not in vals:
                    vals["dimensional_uom_id"] = product_tmpl_id.dimensional_uom_id.id
                if "product_length" not in vals:
                    vals["product_length"] = product_tmpl_id.product_length
                if "product_height" not in vals:
                    vals["product_height"] = product_tmpl_id.product_height
                if "product_width" not in vals:
                    vals["product_width"] = product_tmpl_id.product_width
        return super().create(vals_list)
