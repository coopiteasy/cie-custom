# Copyright 2017 David Vidal<david.vidal@tecnativa.com>
# Copyright 2017 Tecnativa - Pedro M. Baeza
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class EventTravelExpense(models.Model):
    _inherit = "event.speaker.travel.expense"

    status = fields.Selection(selection_add=[("to_pay_in_hand", "To Pay In Hand")])
