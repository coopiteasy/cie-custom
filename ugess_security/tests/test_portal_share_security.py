from odoo import Command

from .common import CommonCase


class TestPortalShareSecurity(CommonCase):
    def _test_access_portal_share(self, allowed_ops="CRUD", with_user=None):
        self._test_access_model(
            model_obj=self.env["portal.share"],
            allowed_ops=allowed_ops,
            with_user=with_user,
        )
        self._test_access_model(
            model_obj=self.env["portal.wizard"],
            allowed_ops=allowed_ops,
            with_user=with_user,
        )
        self._test_access_model(
            model_obj=self.env["portal.wizard.user"],
            allowed_ops=allowed_ops,
            with_user=with_user,
        )

    def test_access_to_res_partner_category(self):
        logged_user = self.test_logged_user

        # internal user
        self._test_access_portal_share(allowed_ops="", with_user=logged_user)

        # partner_manager should not have access anymore
        logged_user.groups_id = [
            Command.link(self.env.ref("base.group_partner_manager").id),
        ]
        self._test_access_portal_share(allowed_ops="", with_user=logged_user)

        # with ugess_security.group_portal_share_manager should CRU
        logged_user.groups_id = [
            Command.unlink(self.env.ref("base.group_partner_manager").id),
            Command.link(self.env.ref("ugess_security.group_portal_share_manager").id),
        ]
        self._test_access_portal_share(allowed_ops="CRU", with_user=logged_user)
