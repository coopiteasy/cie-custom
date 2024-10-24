# SPDX-FileCopyrightText: 2024 Coop IT Easy SC
#
# SPDX-License-Identifier: AGPL-3.0-or-later

from odoo import models


class EventEvent(models.Model):
    _inherit = "event.event"

    def download_track_website_image(self):
        self.ensure_one()
        return {
            "type": "ir.actions.act_url",
            "url": (
                f"/primevere_event_custom/event/{self.id}"
                "/tracks/website_image/download"
            ),
            "target": "self",
        }
