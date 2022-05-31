# Copyright 2020 Coop IT Easy SCRL fs
#   Robin Keunen <robin@coopiteasy.be>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from datetime import date, timedelta

from odoo import api, fields, models

RECENT_DAYS_COUNT = 30


class ProjectProject(models.Model):
    _inherit = "project.project"
    _order = "recent_timesheet_line_count desc, name"

    recent_timesheet_line_count = fields.Integer(
        string="Number of Recent Timesheet Lines",
        compute="_compute_recent_timesheet_line_count",
        store=True,
    )

    @api.depends("analytic_account_id.line_ids")
    @api.multi
    def _compute_recent_timesheet_line_count(self):
        # may lead to performance issues. see with time.
        timesheet_model = self.env["account.analytic.line"]
        start_date = date.today() - timedelta(days=RECENT_DAYS_COUNT)
        for project in self:
            recent_lines = timesheet_model.search(
                [("project_id", "=", project.id), ("date", ">=", start_date)]
            )
            project.recent_timesheet_line_count = len(recent_lines)

    @api.model
    def cron_compute_recent_timesheet_line_count(self):
        projects = self.search([])
        projects._compute_recent_timesheet_line_count()
