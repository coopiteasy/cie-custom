# SPDX-FileCopyrightText: 2024 Coop IT Easy SC
#
# SPDX-License-Identifier: AGPL-3.0-or-later

import csv
import datetime

from odoo import models


class TrackWebsiteExportCSV(models.AbstractModel):
    _name = "report.primevere_event_custom.track_export_website"
    _inherit = "report.report_csv.abstract"

    def generate_csv_report(self, writer, data, event):
        tracks = event.track_ids
        writer.writeheader()
        for track in tracks:
            for date_line in track.dates:
                # Date
                hour = int(date_line.hour)
                minute = round(60 * (date_line.hour - hour))
                track_time = datetime.time(hour=hour, minute=minute)
                # Duration
                hour = int(track.duration)
                minute = round(60 * (track.duration - hour))
                track_duration = datetime.time(hour=hour, minute=minute)
                # Location
                if track.location_id:
                    locations = tuple(map(str.strip, track.location_id.name.split("-")))
                else:
                    locations = ("", "")

                writer.writerow(
                    {
                        "id": date_line.id,
                        "date": date_line.date,
                        "heure": track_time.isoformat(timespec="minutes"),
                        "permanent": int(track.all_event),
                        "lieux_parent": locations[0] if len(locations) > 1 else "",
                        "lieux": locations[-1] if locations else "",
                        "forme": track.format_id.name if track.format_id else "",
                        "duree": track_duration.isoformat(timespec="minutes"),
                        "intervenant court": track.com_info_speaker_short or "",
                        "titre session": track.name or "",
                        "presentation intervenant longue": track.com_info_speaker_long
                        or "",
                        "texte de présentation": track.com_info_event or "",
                        "contact des intervenants": track.com_info_contacts or "",
                        "theme": ",".join(track.theme_ids.mapped("name")),
                        "photo": track.website_image_export_name or "",
                        "age spécifique": track.com_info_age or "",
                        "info dernière minute": track.com_info_note or "",
                    }
                )

    def csv_report_options(self):
        res = super().csv_report_options()
        res["fieldnames"].append("id")
        res["fieldnames"].append("date")
        res["fieldnames"].append("heure")
        res["fieldnames"].append("permanent")
        res["fieldnames"].append("lieux_parent")
        res["fieldnames"].append("lieux")
        res["fieldnames"].append("forme")
        res["fieldnames"].append("duree")
        res["fieldnames"].append("intervenant court")
        res["fieldnames"].append("titre session")
        res["fieldnames"].append("presentation intervenant longue")
        res["fieldnames"].append("texte de présentation")
        res["fieldnames"].append("contact des intervenants")
        res["fieldnames"].append("theme")
        res["fieldnames"].append("photo")
        res["fieldnames"].append("age spécifique")
        res["fieldnames"].append("info dernière minute")
        res["delimiter"] = ";"
        res["quoting"] = csv.QUOTE_NONE
        return res
