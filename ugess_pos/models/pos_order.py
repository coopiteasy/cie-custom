# Copyright 2023 Akretion (https://www.akretion.com).
# @author Pierrick Brun <pierrick.brun@akretion.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class PosOrderLine(models.Model):
    _inherit = "pos.order.line"

    total_without_any_discount = fields.Monetary()


class PosOrder(models.Model):
    _inherit = "pos.order"

    current_membership_line_id = fields.Many2one("membership.membership_line")

    def _order_fields(self, ui_order):
        res = super()._order_fields(ui_order)
        partner = self.env["res.partner"].browse(ui_order.get("partner_id"))
        if partner and partner.current_membership_line_id:
            res["current_membership_line_id"] = partner.current_membership_line_id.id
        return res
