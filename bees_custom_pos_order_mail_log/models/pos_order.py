# SPDX-FileCopyrightText: 2021 Coop IT Easy SC
# SPDX-FileContributor: Robin Keunen <robin@coopiteasy.be>
#
# SPDX-License-Identifier: AGPL-3.0-or-later

from odoo import fields, models


class PosOrder(models.Model):
    _inherit = "pos.order"

    def action_receipt_to_customer(self, name, client, ticket):
        if self:
            message = "{date} UTC Attempting to send mail receipt".format(
                date=fields.datetime.now()
            )
            if self.note:
                self.note = "\n".join((self.note, message))
            else:
                self.note = message

        return super().action_receipt_to_customer(name, client, ticket)
