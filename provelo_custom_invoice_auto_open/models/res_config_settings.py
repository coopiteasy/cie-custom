# Copyright 2023 Coop IT Easy SC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    group_account_invoice_auto_open = fields.Boolean(
        string="Automatically Open Invoices",
        implied_group="provelo_custom_invoice_auto_open"
        ".account_invoice_auto_open_group",
        help="If checked, invoices are automatically "
        "opened when created from sale orders.",
    )
