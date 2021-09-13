# Copyright 2021 Coop IT Easy SCRL fs
#   Robin Keunen <robin@coopiteasy.be>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class PosOrder(models.Model):
    _inherit = "pos.order"

    @api.model
    def send_mail_receipt(self, pos_reference, email, body_from_ui, force=True):
        order = self.search([("pos_reference", "=", pos_reference)])

        if order:
            order.note = "{}\n{} UTC Attempting to send mail receipt ".format(
                order.note or "", fields.datetime.now()
            )

        return super(PosOrder, self).send_mail_receipt(
            pos_reference,
            email,
            body_from_ui,
            force=force,
        )
