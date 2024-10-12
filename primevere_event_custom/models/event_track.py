# SPDX-FileCopyrightText: 2024 Coop IT Easy SC
#
# SPDX-License-Identifier: AGPL-3.0-or-later

from odoo import fields, models


class EventTrack(models.Model):
    _inherit = "event.track"

    theme_ids = fields.Many2many("event.track.theme", string="Themes")
    format_id = fields.Many2one("event.track.format", string="Format")
    commission_summary = fields.Text()
    information = fields.Text()
    contacts = fields.Text()
    all_event = fields.Boolean()
    welcomer_id = fields.Many2one("res.partner", string="Welcomer")
    electricity_watt = fields.Integer()
    com_info_speaker_short = fields.Char(size=50)
    com_info_speaker_long = fields.Text()
    com_info_event = fields.Text()
    com_info_contacts = fields.Text()
    com_info_age = fields.Text()
    com_info_note = fields.Text()
