# Copyright 2022 Coop IT Easy SCRLfs
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import odoo


def migrate(cr, version):
    with odoo.api.Environment.manage():
        env = odoo.api.Environment(cr, odoo.SUPERUSER_ID, {})
        employees = (
            env["hr.employee"]
            .with_context({"active_test": False})
            .search([("user_id", "!=", False)])
        )
        overtime_model = env["hr.timesheet.overtime"]
        for employee in employees:
            overtime_model.create(
                {
                    "employee_id": employee.id,
                }
            )
