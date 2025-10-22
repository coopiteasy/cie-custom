from odoo import Command

from .common import CommonCase


class TestPOSLoyaltySecurity(CommonCase):
    def _test_access_loyalty_card(self, allowed_ops="CRUD", with_user=None):
        self._test_access_model(
            model_obj=self.env["loyalty.card"],
            allowed_ops=allowed_ops,
            with_user=with_user,
        )

    def _test_access_loyalty_programme_and_related(
        self, allowed_ops="CRUD", with_user=None
    ):
        self._test_access_model(
            model_obj=self.env["loyalty.program"],
            allowed_ops=allowed_ops,
            with_user=with_user,
        )
        self._test_access_model(
            model_obj=self.env["loyalty.rule"],
            allowed_ops=allowed_ops,
            with_user=with_user,
        )
        self._test_access_model(
            model_obj=self.env["loyalty.reward"],
            allowed_ops=allowed_ops,
            with_user=with_user,
        )
        self._test_access_model(
            model_obj=self.env["loyalty.mail"],
            allowed_ops=allowed_ops,
            with_user=with_user,
        )

    def test_access_to_pos_loyalty_card(self):
        logged_user = self.test_logged_user

        # internal user cannot access it
        self._test_access_loyalty_card(allowed_ops="", with_user=logged_user)

        # pos user can CRU
        logged_user.groups_id = [
            Command.link(self.env.ref("point_of_sale.group_pos_user").id),
        ]
        self._test_access_loyalty_card(allowed_ops="CRU", with_user=logged_user)

    def test_access_to_loyalty_programme_and_related(self):
        logged_user = self.test_logged_user

        # internal user
        self._test_access_loyalty_programme_and_related(
            allowed_ops="", with_user=logged_user
        )

        # pos manager has full access
        logged_user.groups_id = [
            Command.link(self.env.ref("point_of_sale.group_pos_manager").id),
        ]
        self._test_access_loyalty_programme_and_related(
            allowed_ops="CRUD", with_user=logged_user
        )

        # ugess grocer has full access
        logged_user.groups_id = [
            Command.unlink(self.env.ref("point_of_sale.group_pos_manager").id),
            Command.link(
                self.env.ref("ugess_security.role_ugess_grocer_res_groups").id
            ),
        ]
        self._test_access_loyalty_programme_and_related(
            allowed_ops="CRUD", with_user=logged_user
        )
