# SPDX-FileCopyrightText: 2026 Coop IT Easy SC
#
# SPDX-License-Identifier: AGPL-3.0-or-later

from odoo import fields, models


class AccountMove(models.Model):
    _inherit = "account.move"

    start_date = fields.Date()
    end_date = fields.Date()
