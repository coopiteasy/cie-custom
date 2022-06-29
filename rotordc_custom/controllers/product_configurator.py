# Copyright 2022 Coop IT Easy SC
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import http
from odoo.http import request

from odoo.addons.sale.controllers.product_configurator import (
    ProductConfiguratorController,
)


class RotorDCCustomProductConfiguratorController(ProductConfiguratorController):
    @http.route()
    def get_combination_info(
        self,
        product_template_id,
        product_id,
        combination,
        add_qty,
        pricelist_id,
        **kw,
    ):
        res = super().get_combination_info(
            product_template_id,
            product_id,
            combination,
            add_qty,
            pricelist_id,
            **kw,
        )
        res["barcode"] = (
            request.env["product.product"].browse(res["product_id"]).barcode
        )
        return res
