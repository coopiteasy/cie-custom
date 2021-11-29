# Copyright 2021 Coop IT Easy SCRLfs
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class HrLeaveReport(models.Model):

    _inherit = "hr.leave.report"

    # add this field to allow to filter by it, mainly to be able to exclude
    # leave types with no allocation.
    allocation_type = fields.Selection(
        related="holiday_status_id.allocation_type", readonly=True
    )
