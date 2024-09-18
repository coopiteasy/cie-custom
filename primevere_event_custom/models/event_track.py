# SPDX-FileCopyrightText: 2024 Coop IT Easy SC
#
# SPDX-License-Identifier: AGPL-3.0-or-later

from odoo import fields, models


class EventTrack(models.Model):
    _inherit = "event.track"

    commission_summary = fields.Text()
    information = fields.Text()
    contacts = fields.Text()
    all_event = fields.Boolean()
    # all_event = fields.Boolean(compute="_compute_all_event", store=True)
    welcomer_id = fields.Many2one("res.partner", string="Welcomer")
    electricity_watt = fields.Integer()
    com_info_speaker_short = fields.Char(size=50)
    com_info_speaker_long = fields.Char(size=300)
    com_info_event = fields.Char(size=800)
    com_info_contacts = fields.Text()
    com_info_age = fields.Text()
    com_info_note = fields.Text()

    # @api.depends("event_id.date_begin", "event_id.date_end")
    # def _compute_all_event(self):
    #     self.all_event = False
    #     date_begin = self.event_id.date_begin.to_date()
    #     date_end = self.event_id.date_end.to_date()
    #     delta = date_end-date_begin
    #     if delta.days < 0:
    #         days = []
    #     for n in range(delta.days + 1):
    #         days.append(date_begin + timedelta(days=n))
    #     if days == self.date:
    #         self.all_event = True
