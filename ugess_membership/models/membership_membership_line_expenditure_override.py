# SPDX-FileCopyrightText: 2022 Coop IT Easy SC
#
# SPDX-License-Identifier: AGPL-3.0-or-later


from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class ExpenditureOverride(models.Model):
    """The philosophy of the expenditure override is that it changes the
    expenditure ceiling for a given period (or several periods) within a
    membership. For example, if someone's weekly expenditure ceiling is normally
    100€, it might be 150€ by exception for a defined week.
    """

    # TODO: Very long model name. Can we shorten this?
    _name = "membership.membership_line.expenditure.override"
    _description = "Membership Expenditure Override"
    _order = "date_from asc"

    membership_line_id = fields.Many2one(
        comodel_name="membership.membership_line",
        string="Membership",
        required=True,
    )
    membership_line_date_from = fields.Date(
        string="Membership Start Date", related="membership_line_id.date_from"
    )
    membership_line_date_to = fields.Date(
        string="Membership End Date", related="membership_line_id.date_to"
    )
    date_from = fields.Date(string="Start Date", required=True)
    date_to = fields.Date(string="End Date", required=True)
    expenditure_ceiling_period = fields.Selection(
        related="membership_line_id.expenditure_ceiling_period",
    )
    expenditure_ceiling = fields.Monetary(
        string="New Expenditure Ceiling",
        help="New ceiling for the defined period.",
        required=True,
    )
    currency_id = fields.Many2one(
        comodel_name="res.currency",
        related="membership_line_id.currency_id",
        readonly=True,
    )

    @api.onchange("date_from")
    def _onchange_date_from(self):
        if self.date_from:
            _, date_to = self.env["membership.membership_line"].get_period_range(
                self.date_from, self.expenditure_ceiling_period
            )
            self.date_to = date_to

    @api.constrains(
        "date_from",
        "date_to",
    )
    def _check_valid_period(self):
        for override in self:
            if override.date_from > override.date_to:
                raise ValidationError(
                    _(
                        "The override's start date (%(date_from)s) must be before"
                        " the end date (%(date_to)s)."
                    )
                    % {"date_from": override.date_from, "date_to": override.date_to}
                )
            if (
                override.membership_line_date_from
                and override.date_from < override.membership_line_date_from
            ):
                raise ValidationError(
                    _(
                        "The override's start date (%(date_from)s) must not be"
                        " before the membership's start date (%(line_date_from)s)."
                    )
                    % {
                        "date_from": override.date_from,
                        "line_date_from": override.membership_line_date_from,
                    }
                )
            if (
                override.membership_line_date_to
                and override.date_to > override.membership_line_date_to
            ):
                raise ValidationError(
                    _(
                        "The override's end date (%(date_to)s) must not be after"
                        " the membership's end date (%(line_date_to)s)."
                    )
                    % {
                        "date_to": override.date_to,
                        "line_date_to": override.membership_line_date_to,
                    }
                )
            first_day_matches = self.env[
                "membership.membership_line"
            ].is_first_day_of_period(
                override.date_from, override.expenditure_ceiling_period
            )
            last_day_matches = self.env[
                "membership.membership_line"
            ].is_last_day_of_period(
                override.date_to, override.expenditure_ceiling_period
            )
            date_range_matches = first_day_matches and last_day_matches
            if not date_range_matches:
                if (
                    (
                        date_to_is_equal := override.date_to
                        == override.membership_line_date_to
                    )
                    and first_day_matches
                    or (
                        date_from_is_equal := override.date_from
                        == override.membership_line_date_from
                    )
                    and last_day_matches
                    or date_to_is_equal
                    and date_from_is_equal
                ):
                    # Nothing to do; this is an override from the first day
                    # and/or to the last day of the membership.
                    #
                    # TODO: It is possible that this constraint may be
                    # invalidated if the membership line's date_from is changed.
                    pass
                elif override.expenditure_ceiling_period == "week":
                    raise ValidationError(
                        _(
                            "The override's start date (%(date_from)s) must be"
                            " on a Monday, and the end date (%(date_to)s) must"
                            " be on a Sunday."
                        )
                        % {"date_from": override.date_from, "date_to": override.date_to}
                    )
                elif override.expenditure_ceiling_period == "month":
                    raise ValidationError(
                        _(
                            "The override's start date (%(date_from)s) must be"
                            " on the first day of the month, and the end date"
                            " (%(date_to)s) must be the last."
                        )
                        % {"date_from": override.date_from, "date_to": override.date_to}
                    )
                elif override.expenditure_ceiling_period == "year":
                    raise ValidationError(
                        _(
                            "The override's start date (%(date_from)s) must be"
                            " the first day of the year, and the end date"
                            " (%(date_to)s) must be the last."
                        )
                        % {"date_from": override.date_from, "date_to": override.date_to}
                    )
            other_overrides = self.search(
                [
                    ("membership_line_id", "=", override.membership_line_id.id),
                    ("id", "!=", override.id),
                ]
            )
            for other in other_overrides:
                for date, other_date in zip(
                    (override.date_from, override.date_to),
                    (other.date_from, other.date_to),
                ):
                    if (
                        other.date_from <= date <= other.date_to
                        or override.date_from <= other_date <= override.date_to
                    ):
                        raise ValidationError(
                            _(
                                "The override's date range"
                                " (%(date_from)s–%(date_to)s) overlaps with"
                                " another override's"
                                "(%(other_date_from)s–%(other_date_to)s)."
                            )
                            % {
                                "date_from": override.date_from,
                                "date_to": override.date_to,
                                "other_date_from": other.date_from,
                                "other_date_to": other.date_to,
                            }
                        )
