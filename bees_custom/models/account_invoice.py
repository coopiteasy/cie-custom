# Copyright 2021 Coop IT Easy SCRL fs
#   Robin Keunen <robin@coopiteasy.be>
#   Houssine Bakkali <houssine@coopiteasy.be>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import api, models


class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    # do not recompute date_due if already set
    @api.onchange("payment_term_id", "date_invoice")
    def _onchange_payment_term_date_invoice(self):
        if self.date_due:
            # needed dummy update
            self.date_due = self.date_due
        else:
            super(AccountInvoice, self)._onchange_payment_term_date_invoice()
