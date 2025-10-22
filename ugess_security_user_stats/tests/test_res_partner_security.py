# Copyright 2023 Akretion (http://www.akretion.com).
# @author Olivier Nibart <olivier.nibart@akretion.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo import Command
from odoo.exceptions import AccessError

from .common import CommonCase


class TestResPartnerSecurity(CommonCase):
    def _test_access_res_partner_job_position(self, allowed_ops="CRUD", with_user=None):
        self._test_access_model(
            model_obj=self.env["res.partner.job_position"],
            allowed_ops=allowed_ops,
            with_user=with_user,
        )

    def _test_access_res_partner_category(self, allowed_ops="CRUD", with_user=None):
        self._test_access_model(
            model_obj=self.env["res.partner.category"],
            allowed_ops=allowed_ops,
            with_user=with_user,
        )

    def test_access_to_res_partner_job_position(self):
        logged_user = self.test_logged_user

        # internal user
        self._test_access_res_partner_job_position(
            allowed_ops="", with_user=logged_user
        )

        # partner_manager should have no rights
        logged_user.groups_id = [
            Command.link(self.env.ref("base.group_partner_manager").id),
        ]
        self._test_access_res_partner_job_position(
            allowed_ops="", with_user=logged_user
        )

        # with ugess_partner_household.group_ugess_partner_household_manager should CRUD
        logged_user.groups_id = [
            Command.unlink(self.env.ref("base.group_partner_manager").id),
            Command.link(
                self.env.ref(
                    "ugess_partner_household.group_ugess_partner_household_manager"
                ).id
            ),
        ]
        self._test_access_res_partner_job_position(
            allowed_ops="CRUD", with_user=logged_user
        )

    def test_access_to_res_partner_category(self):
        logged_user = self.test_logged_user

        # internal user
        self._test_access_res_partner_category(allowed_ops="R", with_user=logged_user)

        # partner_manager should have no CUD
        logged_user.groups_id = [
            Command.link(self.env.ref("base.group_partner_manager").id),
        ]
        self._test_access_res_partner_category(allowed_ops="R", with_user=logged_user)

        # with ugess_security.group_res_partner_settings_manager should CRUD
        logged_user.groups_id = [
            Command.unlink(self.env.ref("base.group_partner_manager").id),
            Command.link(
                self.env.ref("ugess_security.group_res_partner_settings_manager").id
            ),
        ]
        self._test_access_res_partner_category(
            allowed_ops="CRUD", with_user=logged_user
        )

    def test_archive_unarchive_right(self):
        logged_user = self.test_logged_user
        a_partner = self.env["res.partner"].create(
            {
                "name": "John Doe",
            }
        )

        # partner_manager should NOT have the right even with
        # ugess_security.group_user_all_non_private_contacts
        logged_user.groups_id = [
            Command.link(
                self.env.ref("ugess_security.group_user_all_non_private_contacts").id
            ),
            Command.link(self.env.ref("base.group_partner_manager").id),
        ]
        with self.assertRaises(AccessError):
            a_partner.with_user(logged_user).action_archive()
        with self.assertRaises(AccessError):
            a_partner.with_user(logged_user).action_unarchive()

        # but with group_res_partner_archive it does
        # (and with ugess_security.group_user_all_contacts)
        logged_user.groups_id = [
            Command.link(self.env.ref("ugess_security.group_res_partner_archive").id),
        ]
        a_partner.with_user(logged_user).action_archive()
        a_partner.with_user(logged_user).action_unarchive()
