# SPDX-FileCopyrightText: 2023 Coop IT Easy SC
#
# SPDX-License-Identifier: AGPL-3.0-or-later

from odoo import fields, models


class SaleOrderGroup(models.Model):
    _name = "sale.order.group"
    _description = "A group of related sale orders"

    sale_order_ids = fields.One2many(
        comodel_name="sale.order",
        inverse_name="sale_order_group_id",
    )
