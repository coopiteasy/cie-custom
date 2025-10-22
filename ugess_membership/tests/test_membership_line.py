# SPDX-FileCopyrightText: 2022 Coop IT Easy SC
#
# SPDX-License-Identifier: AGPL-3.0-or-later

from freezegun import freeze_time

from odoo import fields
from odoo.exceptions import UserError

from .common import UgessMembershipCommon


class TestMembershipLineComputedFields(UgessMembershipCommon):
    @freeze_time("2022-02-04")
    def test_current_period_dates_week_first_period(self):
        self.assertEqual(
            self.membership_line_id.expenditure_ceiling_current_period_start_date,
            self.membership_line_id.date_from,
        )

    @freeze_time("2022-02-11")
    def test_current_period_dates_week_later_period(self):
        self.assertEqual(
            self.membership_line_id.expenditure_ceiling_current_period_start_date,
            # Monday of that week.
            fields.date(2022, 2, 7),
        )
        self.assertEqual(
            self.membership_line_id.expenditure_ceiling_current_period_end_date,
            # Sunday of that week.
            fields.date(2022, 2, 13),
        )

    @freeze_time("2023-02-01")
    def test_current_period_dates_week_last_period(self):
        self.assertEqual(
            self.membership_line_id.expenditure_ceiling_current_period_end_date,
            self.membership_line_id.date_to,
        )

    @freeze_time("2022-02-04")
    def test_current_period_dates_month_first_period(self):
        self.membership_line_id.expenditure_ceiling_period = "month"
        self.assertEqual(
            self.membership_line_id.expenditure_ceiling_current_period_start_date,
            self.membership_line_id.date_from,
        )

    @freeze_time("2022-03-04")
    def test_current_period_dates_month_later_period(self):
        self.membership_line_id.expenditure_ceiling_period = "month"
        self.assertEqual(
            self.membership_line_id.expenditure_ceiling_current_period_start_date,
            fields.date(2022, 3, 1),
        )
        self.assertEqual(
            self.membership_line_id.expenditure_ceiling_current_period_end_date,
            fields.date(2022, 3, 31),
        )

    @freeze_time("2023-02-01")
    def test_current_period_dates_month_last_period(self):
        self.membership_line_id.expenditure_ceiling_period = "month"
        self.assertEqual(
            self.membership_line_id.expenditure_ceiling_current_period_end_date,
            self.membership_line_id.date_to,
        )

    @freeze_time("2022-02-04")
    def test_current_period_dates_year_first_period(self):
        self.membership_line_id.expenditure_ceiling_period = "year"
        self.assertEqual(
            self.membership_line_id.expenditure_ceiling_current_period_start_date,
            self.membership_line_id.date_from,
        )

    @freeze_time("2023-01-04")
    def test_current_period_dates_year_later_period(self):
        self.membership_line_id.expenditure_ceiling_period = "year"
        self.assertEqual(
            self.membership_line_id.expenditure_ceiling_current_period_start_date,
            fields.date(2023, 1, 1),
        )
        # Membership ends before end of next year.
        self.assertEqual(
            self.membership_line_id.expenditure_ceiling_current_period_end_date,
            self.membership_line_id.date_to,
        )
        # Let's extend the membership and then check the current period end
        # date.
        self.membership_line_id.date_to = fields.date(2025, 1, 1)
        self.assertEqual(
            self.membership_line_id.expenditure_ceiling_current_period_end_date,
            fields.date(2023, 12, 31),
        )

    @freeze_time("2023-02-01")
    def test_current_period_dates_year_last_period(self):
        self.membership_line_id.expenditure_ceiling_period = "year"
        self.assertEqual(
            self.membership_line_id.expenditure_ceiling_current_period_end_date,
            self.membership_line_id.date_to,
        )

    @freeze_time("2022-02-11")
    def test_current_ceiling_simple(self):
        self.assertEqual(
            self.membership_line_id.expenditure_ceiling_current,
            100,
        )


class TestMembershipLineConstrains(UgessMembershipCommon):
    def test_create_several_membership_line_same_date(self):
        with self.assertRaises(UserError):
            self.env["membership.membership_line"].create(
                {
                    "membership_id": self.membership_id.id,
                    "partner": self.partner_id.id,
                    "member_price": 1,
                    "date_from": fields.date(2022, 8, 3),
                    "date_to": fields.date(2023, 8, 3),
                }
            )

    def test_create_several_membership_line_same_date2(self):
        with self.assertRaises(UserError):
            self.env["membership.membership_line"].create(
                {
                    "membership_id": self.membership_id.id,
                    "partner": self.partner_id.id,
                    "member_price": 1,
                    "date_from": fields.date(2021, 8, 3),
                    "date_to": fields.date(2022, 8, 3),
                }
            )

    def test_create_several_membership_line_different_date(self):
        self.env["membership.membership_line"].create(
            {
                "membership_id": self.membership_id.id,
                "partner": self.partner_id.id,
                "member_price": 1,
                "date_from": fields.date(2023, 2, 4),
                "date_to": fields.date(2024, 2, 3),
            }
        )
