# Copyright 2017 David Vidal<david.vidal@tecnativa.com>
# Copyright 2017 Tecnativa - Pedro M. Baeza
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class EventTravelBooking(models.Model):
    _inherit = "event.speaker.travel.booking"

    constraints = fields.Text()
    discount_info = fields.Text()
