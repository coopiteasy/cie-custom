# SPDX-FileCopyrightText: 2022 Coop IT Easy SC
#
# SPDX-License-Identifier: AGPL-3.0-or-later

from calendar import monthrange

from odoo import _, api, fields, models
from odoo.exceptions import UserError

# These help strings are reused in the wizard.
EXPENDITURE_CEILING_HELP = """
    This amount represents the maximum amount that can be spent over the period
    given in the expenditure ceiling period field.
    """
EXPENDITURE_CEILING_PERIOD_HELP = """
    This interval represents the period for which the expenditure ceiling is
    defined.

    - Each week starts on a Monday.
    - Each month starts on its first day.
    - Each year starts on its first day.
    """


class MembershipLine(models.Model):
    _inherit = "membership.membership_line"

    social_project_id = fields.Many2one(
        comodel_name="social.project",
        string="Social Project",
        domain="[('partner_id', '=', partner)]",
    )
    social_project_type_id = fields.Many2one(
        comodel_name="social.project.type",
        string="Social Project Type",
        related="social_project_id.type_id",
    )
    comment = fields.Text()
    currency_id = fields.Many2one(
        comodel_name="res.currency",
        related="company_id.currency_id",
        readonly=True,
    )
    expenditure_ceiling = fields.Monetary(
        help=EXPENDITURE_CEILING_HELP,
    )
    expenditure_ceiling_period = fields.Selection(
        selection=[
            ("week", "Week"),
            ("month", "Month"),
            ("year", "Year"),
        ],
        help=EXPENDITURE_CEILING_PERIOD_HELP,
        default="month",
        required=True,
    )
    expenditure_override_ids = fields.One2many(
        comodel_name="membership.membership_line.expenditure.override",
        inverse_name="membership_line_id",
        string="Expenditure Overrides",
    )

    # Computed fields for convenience. These aren't meant to be user-facing.

    expenditure_ceiling_current_period_start_date = fields.Date(
        string="Start Date of Current Period",
        compute="_compute_expenditure_ceiling_fields",
        store=False,
    )
    expenditure_ceiling_current_period_end_date = fields.Date(
        string="End Date of Current Period",
        compute="_compute_expenditure_ceiling_fields",
        store=False,
    )
    expenditure_ceiling_current = fields.Monetary(
        string="Current Expenditure Ceiling",
        compute="_compute_expenditure_ceiling_fields",
        store=False,
    )

    @api.constrains("partner", "date_from", "date_to", "membership_id")
    def _check_membership_do_not_overlap(self):
        for partner in self.mapped("partner"):
            for membership_type in partner.member_lines.mapped("membership_id"):
                lines = partner.member_lines.filtered(
                    lambda l: l.membership_id == membership_type
                )
                for line in lines:
                    for line_compare in lines.filtered(lambda l: l.id != line.id):
                        if (
                            line.date_from
                            and line.date_to
                            and line_compare.date_from
                            and line_compare.date_to
                        ) and (
                            line.date_from <= line_compare.date_to
                            and line.date_to >= line_compare.date_from
                        ):
                            # If any date is None: do not raise error
                            # If dates overlap: raise error
                            raise UserError(
                                _(
                                    "A partner can not have several "
                                    "memberships for the same date and "
                                    "the same membership type."
                                )
                            )

    @api.depends(
        "date_from",
        "date_to",
        "expenditure_ceiling",
        "expenditure_ceiling_period",
        "expenditure_override_ids",
        "expenditure_override_ids.date_to",
        "expenditure_override_ids.date_from",
        "expenditure_override_ids.expenditure_ceiling",
    )
    def _compute_expenditure_ceiling_fields(self):
        today = fields.date.today()
        for line in self:
            override = line.expenditure_override_ids.filtered(
                lambda item: item.date_to >= today and item.date_from <= today
            )
            if override:
                date_from = override.date_from
                date_to = override.date_to
                ceiling = override.expenditure_ceiling
            else:
                ceiling = line.expenditure_ceiling
                date_from, date_to = self.get_period_range(
                    today, line.expenditure_ceiling_period
                )
                # Sanity checks, needed for the first and last period.
                if line.date_from and date_from < line.date_from:
                    date_from = line.date_from
                if line.date_to and date_to > line.date_to:
                    date_to = line.date_to
            line.expenditure_ceiling_current_period_start_date = date_from
            line.expenditure_ceiling_current_period_end_date = date_to
            line.expenditure_ceiling_current = ceiling

    @api.onchange("social_project_id")
    def _onchange_social_project_id(self):
        self.date_from = self.social_project_id.start_date
        self.date_to = self.social_project_id.end_date

    @api.model
    def get_period_range(self, date, period):
        """For a date in a period, get the start date and end date."""
        if period == "week":
            year, week, _ = date.isocalendar()
            # 1 = Monday, 1-indexed
            # TODO: Make this configurable?
            date_from = fields.date.fromisocalendar(year, week, 1)
            date_to = fields.date.fromisocalendar(year, week, 7)
        elif period == "month":
            date_from = fields.date(date.year, date.month, 1)
            _, last_day = monthrange(date.year, date.month)
            date_to = fields.date(date.year, date.month, last_day)
        elif period == "year":
            date_from = fields.date(date.year, 1, 1)
            date_to = fields.date(date.year, 12, 31)
        if date_from and date_to:
            return date_from, date_to
        raise ValueError(_("Period '%s' is invalid.") % period)

    @api.model
    def is_first_day_of_period(self, date, period):
        date_from, _ = self.get_period_range(date, period)
        return date == date_from

    @api.model
    def is_last_day_of_period(self, date, period):
        _, date_to = self.get_period_range(date, period)
        return date == date_to
