# SPDX-FileCopyrightText: 2024 Coop IT Easy SC
#
# SPDX-License-Identifier: AGPL-3.0-or-later

from odoo import fields, models


class EventTrackSpeakerTravelBooking(models.Model):
    _inherit = "event.track.speaker.travel.booking"

    constraints = fields.Text()
    discount_info = fields.Text()