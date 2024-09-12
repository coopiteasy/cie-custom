# Copyright 2017 David Vidal<david.vidal@tecnativa.com>
# Copyright 2017 Tecnativa - Pedro M. Baeza
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class EventTrackSpeaker(models.Model):
    _inherit = "event.track.speaker"

    curriculum_vitae = fields.Text()
    invitation_number = fields.Integer()
    invitation_code = fields.Integer()
    need_ticket = fields.Boolean()
    need_reserved_car_place = fields.Boolean()
    slot_wishes = fields.Text()
