# SPDX-FileCopyrightText: 2022 Coop IT Easy SC
#
# SPDX-License-Identifier: AGPL-3.0-or-later

from datetime import date

from freezegun import freeze_time

from odoo.exceptions import ValidationError
from odoo.tests.common import Form

from .common import UgessMembershipCommon


class TestExpenditureOverride(UgessMembershipCommon):
    @freeze_time("2022-02-04")
    def test_override_first_period(self):
        """You can create an override from the first day of a membership to the
        end of that period.
        """
        self._create_expenditure_override("2022-02-03", "2022-02-06")
        self.assertEqual(
            self.membership_line_id.expenditure_ceiling_current,
            50,
        )

    @freeze_time("2023-02-01")
    def test_override_last_period(self):
        """You can create an override from the first day of the last period to
        the end of the membership.
        """
        self._create_expenditure_override("2023-01-30", "2023-02-03")
        self.assertEqual(
            self.membership_line_id.expenditure_ceiling_current,
            50,
        )

    @freeze_time("2022-02-11")
    def test_simple_override_ceiling(self):
        """A simple test case for an overridden ceiling."""
        self._create_expenditure_override("2022-02-07", "2022-02-13")
        self.assertEqual(self.partner_id.expenditure_ceiling_current, 50)

    @freeze_time("2022-03-01")
    def test_override_not_active_period(self):
        """Override doesn't apply to current period."""
        self._create_expenditure_override("2022-02-07", "2022-02-13")
        self.assertEqual(self.partner_id.expenditure_ceiling_current, 100)

    @freeze_time("2022-02-11")
    def test_override_change_ceiling(self):
        """Retroactively changing the ceiling on an override changes the current
        ceiling.
        """
        override = self._create_expenditure_override("2022-02-07", "2022-02-13")
        self.assertEqual(self.partner_id.expenditure_ceiling_current, 50)
        override.expenditure_ceiling = 200
        self.assertEqual(self.partner_id.expenditure_ceiling_current, 200)

    @freeze_time("2022-03-04")
    def test_onchange_date_from(self):
        """When changing date_from, set date_to to last day in date_from's
        period.
        """
        override_form = Form(
            self.env["membership.membership_line.expenditure.override"].with_context(
                default_membership_line_id=self.membership_line_id.id
            )
        )
        override_form.date_from = "2022-03-14"
        self.assertEqual(override_form.date_to, date(2022, 3, 20))


class TestExpenditureOverrideConstraint(UgessMembershipCommon):
    def test_first_period_start_must_be_start(self):
        """The start of the first period must be the start of the membership,
        not the start of the period, which is before the membership's start.
        """
        with self.assertRaises(ValidationError):
            self._create_expenditure_override("2022-01-31", "2022-02-06")

    def test_end_before_start(self):
        """The override's end date cannot be before the override's start date."""
        with self.assertRaises(ValidationError):
            self._create_expenditure_override(
                # A Monday
                "2022-02-14",
                # A Sunday
                "2022-02-06",
            )

    def test_start_before_membership_start(self):
        """The override's start date cannot be before the membership's."""
        with self.assertRaises(ValidationError):
            self._create_expenditure_override(
                # A Monday
                "2021-02-01",
                # A Sunday
                "2021-02-07",
            )

    def test_end_before_membership_end(self):
        """The override's end date cannot be after the membership's."""
        with self.assertRaises(ValidationError):
            self._create_expenditure_override(
                # A Monday
                "2023-02-13",
                # A Sunday
                "2023-02-19",
            )

    def test_multiple_periods(self):
        """An override can span multiple periods."""
        self._create_expenditure_override(
            # A Monday
            "2022-02-07",
            # A Sunday
            "2022-02-20",
        )

    def test_multiple_periods_first_period(self):
        """An override can span multiple periods from the first period."""
        self._create_expenditure_override("2022-02-03", "2022-02-13")

    def test_multiple_periods_last_period(self):
        """An override can span multiple periods to the last period."""
        self._create_expenditure_override("2022-02-14", "2023-02-03")

    def test_multiple_periods_first_to_last(self):
        """An override can span first date to last date."""
        self._create_expenditure_override("2022-02-03", "2023-02-03")

    def test_multiple_overrides(self):
        """There can be multiple overrides on a membership."""
        # Using a single create() to implicitly test the for-loop in the
        # constraint method.
        self.env["membership.membership_line.expenditure.override"].create(
            [
                {
                    "membership_line_id": self.membership_line_id.id,
                    # A Monday
                    "date_from": "2022-02-07",
                    # A Sunday
                    "date_to": "2022-02-13",
                    "expenditure_ceiling": 50,
                },
                {
                    "membership_line_id": self.membership_line_id.id,
                    # A Monday
                    "date_from": "2022-02-14",
                    # A Sunday
                    "date_to": "2022-02-20",
                    "expenditure_ceiling": 50,
                },
            ]
        )

    def test_no_overlap(self):
        """Overrides cannot overlap."""
        self._create_expenditure_override(
            # A Monday
            "2022-03-07",
            # A Sunday
            "2022-03-20",
        )
        # Start date in previous range
        with self.assertRaises(ValidationError):
            self._create_expenditure_override(
                # A Monday
                "2022-03-14",
                # A Sunday
                "2022-03-27",
            )

        # End date in previous range
        with self.assertRaises(ValidationError):
            self._create_expenditure_override(
                # A Monday
                "2022-02-28",
                # A Sunday
                "2022-03-13",
            )
        # Identical range
        with self.assertRaises(ValidationError):
            self._create_expenditure_override(
                # A Monday
                "2022-03-07",
                # A Sunday
                "2022-03-20",
            )
        # Range envelops previous range
        with self.assertRaises(ValidationError):
            self._create_expenditure_override(
                # A Monday
                "2022-02-28",
                # A Sunday
                "2022-03-27",
            )

    def test_week_correct(self):
        """No ValidationError when giving correct dates for a weekly override."""
        self._create_expenditure_override(
            # A Monday
            "2022-02-07",
            # A Sunday
            "2022-02-13",
        )

    def test_week_start_not_monday(self):
        """The weekly override's start day must be a Monday."""
        with self.assertRaises(ValidationError):
            self._create_expenditure_override(
                # A Tuesday
                "2022-02-08",
                # A Sunday
                "2022-02-13",
            )

    def test_week_end_not_sunday(self):
        """The weekly override's end day must be a Sunday."""
        with self.assertRaises(ValidationError):
            self._create_expenditure_override(
                # A Monday
                "2022-02-07",
                # A Saturday
                "2022-02-12",
            )

    def test_month_correct(self):
        """No ValidationError when giving correct dates for a monthly override."""
        self.membership_line_id.expenditure_ceiling_period = "month"

        self._create_expenditure_override(
            "2022-03-01",
            "2022-03-31",
        )

    def test_month_start_not_first(self):
        """The monthly override's start date must be the first of the month."""
        self.membership_line_id.expenditure_ceiling_period = "month"
        with self.assertRaises(ValidationError):
            self._create_expenditure_override(
                "2022-03-02",
                "2022-03-31",
            )

    def test_month_end_not_last(self):
        """The monthly override's end date must be the last of the month."""
        self.membership_line_id.expenditure_ceiling_period = "month"
        with self.assertRaises(ValidationError):
            self._create_expenditure_override(
                "2022-03-01",
                "2022-03-30",
            )
        with self.assertRaises(ValidationError):
            self._create_expenditure_override(
                "2022-04-01",
                "2022-04-29",
            )

    def test_year_correct(self):
        """No ValidationError when giving correct dates for a yearly override."""
        self.membership_line_id.expenditure_ceiling_period = "year"
        self.membership_line_id.date_to = "2030-12-31"
        self._create_expenditure_override(
            "2023-01-01",
            "2023-12-31",
        )

    def test_year_start_not_first(self):
        """The yearly override's start date must be the first of the year."""
        self.membership_line_id.expenditure_ceiling_period = "year"
        self.membership_line_id.date_to = "2030-12-31"
        with self.assertRaises(ValidationError):
            self._create_expenditure_override(
                "2023-01-02",
                "2023-12-31",
            )

    def test_year_end_not_last(self):
        """The yearly override's end date must be the last of the year."""
        self.membership_line_id.expenditure_ceiling_period = "year"
        self.membership_line_id.date_to = "2030-12-31"
        with self.assertRaises(ValidationError):
            self._create_expenditure_override(
                "2023-01-01",
                "2023-12-30",
            )
