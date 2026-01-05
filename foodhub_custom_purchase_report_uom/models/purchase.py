# SPDX-FileCopyrightText: 2025 Coop IT Easy SC
#
# SPDX-License-Identifier: AGPL-3.0-or-later

from odoo import fields, models


class PurchaseOrderLine(models.Model):
    _inherit = "purchase.order.line"

    # Used for the report/purchase_order_templates.xml
    product_main_uom_qty = fields.Float(
        string="Quantity ordered in UoM rather than purchase UoM",
        compute="_compute_product_main_uom_qty",
    )

    def _compute_product_main_uom_qty(self):
        for line in self:
            line.product_main_uom_qty = line.product_id.uom_po_id._compute_quantity(
                line.product_qty,
                line.product_id.uom_id,
            )
