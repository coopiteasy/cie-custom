# SPDX-FileCopyrightText: 2023 Coop IT Easy SC
#
# SPDX-License-Identifier: AGPL-3.0-or-later

from odoo import api, fields, models


class SaleOrderGroup(models.Model):
    _name = "sale.order.group"
    _description = "A group of related sale orders"

    sale_order_ids = fields.One2many(
        comodel_name="sale.order",
        inverse_name="sale_order_group_id",
    )


class SaleOrder(models.Model):
    _inherit = "sale.order"

    sale_order_group_id = fields.Many2one(
        comodel_name="sale.order.group",
    )
    related_so_ids = fields.Many2many(
        string="Linked Sale Orders",
        comodel_name="sale.order",
        compute="_compute_related_sale_orders",
    )

    @api.multi
    def create_related_sale_order(self):
        self.ensure_one()
        if not self.sale_order_group_id:
            self.sale_order_group_id = self.env["sale.order.group"].create({})

        ctx = {
            "default_partner_id": self.partner_id.id,
            "default_origin": self.name,
            "default_sale_order_group_id": self.sale_order_group_id.id,
        }
        return {
            "type": "ir.actions.act_window",
            "view_type": "form",
            "view_mode": "form",
            "res_model": "sale.order",
            "target": "current",
            "context": ctx,
        }

    @api.multi
    @api.depends("sale_order_group_id.sale_order_ids")
    def _compute_related_sale_orders(self):
        for so in self:
            if so.sale_order_group_id:
                so.related_so_ids = so.sale_order_group_id.sale_order_ids.filtered(
                    lambda related_so: related_so != so
                )
