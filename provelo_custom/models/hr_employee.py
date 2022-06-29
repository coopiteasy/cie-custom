# Copyright 2022 Coop IT Easy SC
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, models


class HrEmployee(models.Model):

    _inherit = "hr.employee"

    @api.model
    def create(self, vals):
        # only employees linked to a user can have timesheets.
        create_overtime = vals.get("user_id")
        result = super().create(vals)
        if create_overtime:
            self.env["hr.timesheet.overtime"].create(
                {
                    "employee_id": result.id,
                }
            )
        return result

    @api.multi
    def write(self, vals):
        # only employees linked to a user can have timesheets.
        create_overtime = vals.get("user_id") and not self.user_id
        result = super().write(vals)
        overtime_model = self.env["hr.timesheet.overtime"]
        if create_overtime:
            if not overtime_model.search([("employee_id", "=", self.id)]):
                overtime_model.create(
                    {
                        "employee_id": self.id,
                    }
                )
        return result
