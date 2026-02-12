from odoo import Command

from .common import CommonCase


class TestPointOfSaleSecurity(CommonCase):
    def _test_access_pos_details_wizard(self, allowed_ops="CRUD", with_user=None):
        self._test_access_model(
            model_obj=self.env["pos.details.wizard"],
            allowed_ops=allowed_ops,
            with_user=with_user,
        )

    def _test_access_report_pos_order(self, allowed_ops="CRUD", with_user=None):
        self._test_access_model(
            model_obj=self.env["report.pos.order"],
            allowed_ops=allowed_ops,
            with_user=with_user,
        )

    def _test_access_pos_payment_change(self, allowed_ops="CRUD", with_user=None):
        self._test_access_model(
            model_obj=self.env["pos.payment.change.wizard"],
            allowed_ops=allowed_ops,
            with_user=with_user,
        )
        self._test_access_model(
            model_obj=self.env["pos.payment.change.wizard.new.line"],
            allowed_ops=allowed_ops,
            with_user=with_user,
        )
        self._test_access_model(
            model_obj=self.env["pos.payment.change.wizard.old.line"],
            allowed_ops=allowed_ops,
            with_user=with_user,
        )

    def _test_access_pos_make_payment(self, allowed_ops="CRUD", with_user=None):
        self._test_access_model(
            model_obj=self.env["pos.make.payment"],
            allowed_ops=allowed_ops,
            with_user=with_user,
        )

    def test_access_to_pos_details_wizard(self):
        logged_user = self.test_logged_user

        # internal user
        self._test_access_pos_details_wizard(allowed_ops="", with_user=logged_user)

        # pos user can access this report
        logged_user.groups_id = [
            Command.link(self.env.ref("point_of_sale.group_pos_user").id),
        ]
        self._test_access_pos_details_wizard(allowed_ops="CRU", with_user=logged_user)

    def test_access_to_report_pos_order(self):
        logged_user = self.test_logged_user

        # internal user
        self._test_access_report_pos_order(allowed_ops="", with_user=logged_user)

        # pos user can't access this report
        logged_user.groups_id = [
            Command.link(self.env.ref("point_of_sale.group_pos_user").id),
        ]
        self._test_access_report_pos_order(allowed_ops="", with_user=logged_user)

        # pos manager can access this report
        logged_user.groups_id = [
            Command.link(self.env.ref("point_of_sale.group_pos_manager").id),
        ]
        self._test_access_report_pos_order(allowed_ops="CRUD", with_user=logged_user)

        # ugess grocer can access this report
        logged_user.groups_id = [
            Command.unlink(self.env.ref("point_of_sale.group_pos_manager").id),
            Command.link(
                self.env.ref("ugess_security.role_ugess_grocer_res_groups").id
            ),
        ]
        self._test_access_report_pos_order(allowed_ops="CRUD", with_user=logged_user)

    def test_access_to_report_pos_payment_change(self):
        logged_user = self.test_logged_user

        # internal user
        self._test_access_pos_payment_change(allowed_ops="R", with_user=logged_user)

        # pos manager can change payment
        logged_user.groups_id = [
            Command.link(self.env.ref("point_of_sale.group_pos_manager").id),
        ]
        self._test_access_pos_payment_change(allowed_ops="CRUD", with_user=logged_user)

        # ugess grocer can change payment
        logged_user.groups_id = [
            Command.unlink(self.env.ref("point_of_sale.group_pos_manager").id),
            Command.link(
                self.env.ref("ugess_security.role_ugess_grocer_res_groups").id
            ),
        ]
        self._test_access_pos_payment_change(allowed_ops="CRUD", with_user=logged_user)

    def test_access_to_pos_make_payment(self):
        logged_user = self.test_logged_user

        # internal user
        self._test_access_pos_make_payment(allowed_ops="", with_user=logged_user)

        # pos user can make pos payment
        logged_user.groups_id = [
            Command.link(self.env.ref("point_of_sale.group_pos_user").id),
        ]
        self._test_access_pos_make_payment(allowed_ops="CRU", with_user=logged_user)
