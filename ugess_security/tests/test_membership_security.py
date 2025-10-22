from odoo import Command

from .common import CommonCase


class TestMembershipSecurity(CommonCase):
    def _test_access_membership_products(self, allowed_ops="CRUD", with_user=None):
        self._test_complex_access_model(
            model_obj=self.env["product.template"],
            search_domain=[
                ("membership", "=", True),
            ],
            create_vals={
                "name": "Test Membership for Access Test",
                "membership": True,
                "type": "service",
                "membership_date_from": "1970-01-01",
                "membership_date_to": "1970-01-02",
            },
            write_vals={
                "name": "Test Membership for Access Test Updated",
            },
            allowed_ops=allowed_ops,
            with_user=with_user,
        )

    def _test_access_regular_product_templates(
        self, allowed_ops="CRUD", with_user=None
    ):
        self._test_complex_access_model(
            model_obj=self.env["product.template"],
            search_domain=[
                ("membership", "=", False),
            ],
            create_vals={
                "name": "Test Template for Access Test",
                "membership": False,
                "type": "product",
            },
            write_vals={
                "name": "Test Template for Access Test Updated",
            },
            allowed_ops=allowed_ops,
            with_user=with_user,
        )

    def _test_access_report_membership(self, allowed_ops="CRUD", with_user=None):
        self._test_access_model(
            model_obj=self.env["report.membership"],
            allowed_ops=allowed_ops,
            with_user=with_user,
        )

    def _test_access_membership_category(self, allowed_ops="CRUD", with_user=None):
        self._test_access_model(
            model_obj=self.env["membership.membership_category"],
            allowed_ops=allowed_ops,
            with_user=with_user,
        )

    def _test_access_membership_withdrawal_reason(
        self, allowed_ops="CRUD", with_user=None
    ):
        self._test_access_model(
            model_obj=self.env["membership.withdrawal_reason"],
            allowed_ops=allowed_ops,
            with_user=with_user,
        )

    def test_access_to_memberships_products(self):
        logged_user = self.test_logged_user

        # internal user
        self._test_access_membership_products(allowed_ops="R", with_user=logged_user)
        self._test_access_regular_product_templates(
            allowed_ops="R", with_user=logged_user
        )

        # membership user
        logged_user.groups_id = [
            Command.link(self.env.ref("ugess_security.group_membership_user").id),
        ]
        self._test_access_membership_products(allowed_ops="R", with_user=logged_user)
        self._test_access_regular_product_templates(
            allowed_ops="R", with_user=logged_user
        )

        # with inventory admin right should not CUD on memberships
        logged_user.groups_id = [
            Command.link(self.env.ref("stock.group_stock_manager").id),
        ]
        self._test_access_membership_products(allowed_ops="R", with_user=logged_user)
        self._test_access_regular_product_templates(
            allowed_ops="CRUD", with_user=logged_user
        )

        # membership manager
        logged_user.groups_id = [
            Command.unlink(self.env.ref("ugess_security.group_membership_user").id),
            Command.unlink(self.env.ref("stock.group_stock_manager").id),
            Command.link(
                self.env.ref("membership_extension.group_membership_manager").id
            ),
        ]
        # with no inventory admin right cannot C because
        # of the access on product variants and this is probabley to fix
        # see the note in security/membership_security.xml
        self._test_access_membership_products(allowed_ops="RUD", with_user=logged_user)
        self._test_access_regular_product_templates(
            allowed_ops="R", with_user=logged_user
        )

        # with inventory admin right should CRUD on everything
        logged_user.groups_id = [
            Command.link(self.env.ref("stock.group_stock_manager").id),
        ]
        self._test_access_membership_products(allowed_ops="CRUD", with_user=logged_user)
        self._test_access_regular_product_templates(
            allowed_ops="CRUD", with_user=logged_user
        )

    def test_access_to_report_membership(self):
        logged_user = self.test_logged_user

        # internal user
        self._test_access_report_membership(allowed_ops="", with_user=logged_user)

        # partner manager
        logged_user.groups_id = [
            Command.link(self.env.ref("base.group_partner_manager").id),
        ]
        self._test_access_report_membership(allowed_ops="", with_user=logged_user)

        # ugess social
        logged_user.groups_id = [
            Command.link(
                self.env.ref("ugess_security.role_ugess_social_res_groups").id
            ),
        ]
        self._test_access_report_membership(allowed_ops="R", with_user=logged_user)

    def test_access_to_membership_category(self):
        logged_user = self.test_logged_user

        # internal user
        self._test_access_membership_category(allowed_ops="R", with_user=logged_user)

        # partner manager cannot CUD
        logged_user.groups_id = [
            Command.link(self.env.ref("base.group_partner_manager").id),
        ]
        self._test_access_membership_category(allowed_ops="R", with_user=logged_user)

        # ugess manager neither
        logged_user.groups_id = [
            Command.link(
                self.env.ref("ugess_security.role_ugess_manager_res_groups").id
            ),
        ]
        self._test_access_membership_category(allowed_ops="R", with_user=logged_user)

        # but ugess partner settings manager yes
        logged_user.groups_id = [
            Command.link(
                self.env.ref("ugess_security.group_res_partner_settings_manager").id
            ),
        ]
        self._test_access_membership_category(allowed_ops="CRUD", with_user=logged_user)

    def test_access_to_membership_withdrawal_reason(self):
        logged_user = self.test_logged_user

        # internal user
        self._test_access_membership_withdrawal_reason(
            allowed_ops="R", with_user=logged_user
        )

        # partner manager cannot CUD
        logged_user.groups_id = [
            Command.link(self.env.ref("base.group_partner_manager").id),
        ]
        self._test_access_membership_withdrawal_reason(
            allowed_ops="R", with_user=logged_user
        )

        # membership manager can CRUD
        logged_user.groups_id = [
            Command.link(
                self.env.ref("membership_extension.group_membership_manager").id
            ),
        ]
        self._test_access_membership_withdrawal_reason(
            allowed_ops="CRUD", with_user=logged_user
        )
