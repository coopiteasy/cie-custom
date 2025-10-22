# SPDX-FileCopyrightText: 2022 Coop IT Easy SC
#
# SPDX-License-Identifier: AGPL-3.0-or-later

from freezegun import freeze_time

from odoo import fields

from .common import UgessMembershipCommon


class TestPartner(UgessMembershipCommon):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

    @freeze_time("2022-02-04")
    def test_current_membership_line_one(self):
        """Given one membership, then that is the current membership."""
        self.assertEqual(
            self.partner_id.current_membership_line_id,
            self.membership_line_id,
        )

    def test_current_membership_line_none(self):
        """Given no membership, then there is no current membership."""
        partner = self.env["res.partner"].create({"name": "John Doe"})
        self.assertFalse(partner.current_membership_line_id)

    @freeze_time("2022-03-04")
    def test_current_membership_line_multi(self):
        """Given multiple memberships, then the most recent date_from is the
        current membership.
        """
        # Create another membership type because overlapping cannot happen
        # For the same membership category
        self.membership_template_2 = self.env["product.template"].create(
            {
                "name": "Test Membership 2",
                "membership_type": "custom",
            }
        )
        self.membership_2 = self.membership_template_2.product_variant_id
        most_recent_line = self.env["membership.membership_line"].create(
            {
                "membership_id": self.membership_2.id,
                "partner": self.partner_id.id,
                "member_price": 1,
                "date_from": fields.date(2022, 3, 3),
                "date_to": fields.date(2023, 4, 3),
                "state": "paid",
            }
        )
        self.membership_template_3 = self.env["product.template"].create(
            {
                "name": "Test Membership 3",
                "membership_type": "custom",
            }
        )
        self.membership_3 = self.membership_template_3.product_variant_id
        # least recent line.
        self.env["membership.membership_line"].create(
            {
                "membership_id": self.membership_3.id,
                "partner": self.partner_id.id,
                "member_price": 1,
                "date_from": fields.date(2022, 1, 3),
                "date_to": fields.date(2023, 2, 3),
                "state": "paid",
            }
        )
        self.assertEqual(
            self.partner_id.current_membership_line_id,
            most_recent_line,
        )

    @freeze_time("2022-03-04")
    def test_search_current_membership_line_id(self):
        current_id = self.partner_id.current_membership_line_id
        result = self.env["res.partner"].search(
            [("current_membership_line_id", "=", current_id.id)]
        )
        self.assertEqual(result.current_membership_line_id, current_id)
