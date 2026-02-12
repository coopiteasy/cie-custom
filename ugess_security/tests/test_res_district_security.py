from odoo import Command

from .common import CommonCase


class TestResDistrictSecurity(CommonCase):
    def _test_access_res_district(self, allowed_ops="CRUD", with_user=None):
        self._test_access_model(
            model_obj=self.env["res.district"],
            allowed_ops=allowed_ops,
            with_user=with_user,
        )

    def test_access_to_res_district(self):
        logged_user = self.test_logged_user

        # internal user
        self._test_access_res_district(allowed_ops="R", with_user=logged_user)

        # partner_manager should have only the R right
        logged_user.groups_id = [
            Command.link(self.env.ref("base.group_partner_manager").id),
        ]
        self._test_access_res_district(allowed_ops="R", with_user=logged_user)

        # with ugess_security.group_res_district_manager should CRUD
        logged_user.groups_id = [
            Command.unlink(self.env.ref("base.group_partner_manager").id),
            Command.link(self.env.ref("ugess_security.group_res_district_manager").id),
        ]
        self._test_access_res_district(allowed_ops="CRUD", with_user=logged_user)
