# SPDX-FileCopyrightText: 2022 Coop IT Easy SC
#
# SPDX-License-Identifier: AGPL-3.0-or-later

from odoo import http
from odoo.http import request

from odoo.addons.website_sale.controllers.main import WebsiteSale


class MissingCategoryException(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args)
        self.unused_categs = kwargs.get("unused_categs")


def _verify_products_have_all_optional_products(env, order):
    """On an order, verify that each product has chosen one optional product of
    each available category to that product.

    Return a Dict[sale.order.line, product.category] with all order lines that
    have missing categories.
    """
    order_line_unused_map = {}
    for order_line in order.order_line:
        try:
            _verify_line(order_line)
        except MissingCategoryException as err:
            order_line_unused_map[order_line] = err.unused_categs
    return order_line_unused_map


def _verify_line(order_line):
    # FIXME: Consider also raising an exception if there is a duplicate encounter.
    categ_ids = {
        template_id.categ_id
        for template_id in order_line.product_id.optional_product_ids
    }
    encountered = {line.product_id.categ_id for line in order_line.option_line_ids}
    # unused_categs is all elements in categ_ids that are not in encountered,
    # NOT the other way around. The other way around is not tested, assuming
    # that Odoo works soundly.
    unused_categs = categ_ids.difference(encountered)
    if unused_categs:
        raise MissingCategoryException(unused_categs=unused_categs)


class WebsiteSaleDelivery(WebsiteSale):
    @http.route()
    def checkout(self, **post):
        order = request.website.sale_get_order()
        result = _verify_products_have_all_optional_products(request.env, order)

        if result:
            return request.render(
                "rotordc_optional_product.missing_categories",
                {
                    "order_line_unused_map": result,
                },
            )

        return super().checkout(**post)
