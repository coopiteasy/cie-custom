# Copyright 2023 Akretion (https://www.akretion.com).
# @author Pierrick Brun <pierrick.brun@akretion.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    current_membership_line_id = fields.Many2one("membership.membership_line")

    def _action_confirm(self):
        res = super()._action_confirm()
        for record in self:
            if record.partner_id and record.partner_id.current_membership_line_id:
                record.current_membership_line_id = (
                    record.partner_id.current_membership_line_id
                )
        return res
