# Copyright 2020 Coop IT Easy SCRL fs
#   Robin Keunen <robin@coopiteasy.be>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import api, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    @api.multi
    def _prepare_invoice(self):
        values = super(SaleOrder, self)._prepare_invoice()

        if self.location_id and self.location_id.journal_id:
            values["journal_id"] = self.location_id.journal_id.id

        return values

    def _create_sale_order(self, activity, partner_id):
        order = super()._create_sale_order(activity, partner_id)
        order.write(
            {
                "project_id": activity.analytic_account.id,
            }
        )
        return order
