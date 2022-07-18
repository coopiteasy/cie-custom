# SPDX-FileCopyrightText: 2022 Coop IT Easy SC
#
# SPDX-License-Identifier: AGPL-3.0-or-later

from odoo import api, models


class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    @api.model
    def create(self, vals):
        # For some reason the comment is not correctly set to the default when
        # invoices are created from the POS. The cause is unknown, but this
        # fixes it.
        #
        # Task 8882.
        if not vals.get("comment"):
            vals["comment"] = self._default_comment()

        return super().create(vals)
