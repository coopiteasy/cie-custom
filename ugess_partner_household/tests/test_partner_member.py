# SPDX-FileCopyrightText: 2022 Coop IT Easy SC
#
# SPDX-License-Identifier: AGPL-3.0-or-later

from odoo.exceptions import UserError
from odoo.fields import date
from odoo.tests.common import TransactionCase


class TestPartnerMember(TransactionCase):
    """Tests for both res.partner and household.member, wrapped up in one."""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.partner = cls.env.ref("ugess_partner_household.partner_household")
        cls.member_mother = cls.env["household.member"].search(
            [("name", "=", cls.partner.name)]
        )
        cls.member_child_1 = cls.env.ref(
            "ugess_partner_household.household_member_child_1"
        )
        cls.member_child_2 = cls.env.ref(
            "ugess_partner_household.household_member_child_2"
        )
        cls.member_child_3 = cls.env.ref(
            "ugess_partner_household.household_member_child_3"
        )

    def test_newly_created_partner_has_linked_member(self):
        partner = self.env["res.partner"].create({"name": "Test"})
        self.assertTrue(partner.linked_household_member_id)

    def test_demo_partner_has_linked_member(self):
        partner = self.env.ref("base.res_partner_address_1")
        self.assertTrue(partner.linked_household_member_id)

    def test_linked_household_member(self):
        self.assertEqual(
            self.partner.linked_household_member_id,
            self.member_mother,
        )
        self.assertTrue(self.member_mother.is_linked_to_partner)
        self.assertFalse(self.member_child_1.is_linked_to_partner)
        self.assertFalse(self.member_child_2.is_linked_to_partner)
        self.assertFalse(self.member_child_3.is_linked_to_partner)

    def test_write_is_propagated(self):
        self.partner.write(
            {
                "name": "Changed",
                "job_position_id": (0, False, {"name": "New"}),
                "main_income_source_member": (0, False, {"name": "New"}),
                "birthdate_date": date(1995, 1, 1),
                "gender": "other",
            }
        )
        self.assertEqual(
            self.partner.name,
            self.partner.linked_household_member_id.name,
        )
        self.assertEqual(
            self.partner.job_position_id,
            self.partner.linked_household_member_id.job_position_id,
        )
        self.assertEqual(
            self.partner.main_income_source_member,
            self.partner.linked_household_member_id.main_income_source,
        )
        self.assertEqual(
            self.partner.birthdate_date,
            self.partner.linked_household_member_id.birthdate_date,
        )
        # Computed field.
        self.assertEqual(
            self.partner.age,
            self.partner.linked_household_member_id.age,
        )
        self.assertEqual(
            self.partner.gender,
            self.partner.linked_household_member_id.gender,
        )
        self.assertNotEqual(
            self.partner.name,
            self.partner.household_member_ids[1].name,
        )

    def test_unlink_first_member(self):
        with self.assertRaises(UserError):
            self.partner.linked_household_member_id.unlink()

    def test_unlink_second_member(self):
        with self.assertRaises(UserError):
            self.member_child_1.unlink()
            self.member_child_2.unlink()
            self.member_child_3.unlink()

    def test_toggle_active_first_member(self):
        with self.assertRaises(UserError):
            self.partner.linked_household_member_id.is_active_member = False

    def test_toggle_active_second_member(self):
        self.member_child_1.is_active_member = False
        self.member_child_2.is_active_member = False
        self.member_child_3.is_active_member = False

    def test_unlink_partner(self):
        self.partner.unlink()
