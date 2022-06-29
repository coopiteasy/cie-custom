# Copyright 2022 Coop IT Easy SC
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import _, fields, models


class HrTimesheetOvertime(models.Model):

    _name = "hr.timesheet.overtime"
    _description = "Overtime"
    _sql_constraints = [
        (
            "employee_id_key",
            "unique (employee_id)",
            _("There can be only one overtime per employee."),
        )
    ]

    name = fields.Char(
        related="employee_id.name",
    )
    active = fields.Boolean(
        related="employee_id.active",
    )
    employee_id = fields.Many2one(
        "hr.employee",
        required=True,
        ondelete="cascade",
    )
    initial_overtime = fields.Float(
        related="employee_id.initial_overtime",
        readonly=False,
        groups="base.group_user",
    )
    total_overtime = fields.Float(
        related="employee_id.total_overtime",
        groups="base.group_user",
    )
    overtime_start_date = fields.Date(
        related="employee_id.overtime_start_date",
        readonly=False,
        groups="base.group_user",
    )
