# SPDX-FileCopyrightText: 2023 Coop IT Easy SC
#
# SPDX-License-Identifier: AGPL-3.0-or-later

from odoo import api, models


class AccountAnalyticLine(models.Model):
    _inherit = "account.analytic.line"

    @api.onchange("project_id")
    def _set_task_domain_on_project_change(self):
        result = super()._set_task_domain_on_project_change()
        if not result["domain"]["task_id"]:
            result["domain"]["task_id"] = [
                ("project_id.project_status.is_closed", "=", False)
            ]
        return result
