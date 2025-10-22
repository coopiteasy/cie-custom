from odoo import Command

from .common import CommonCase


class TestProductSecurity(CommonCase):
    def _test_access_product_tag(self, allowed_ops="CRUD", with_user=None):
        self._test_access_model(
            model_obj=self.env["product.tag"],
            allowed_ops=allowed_ops,
            with_user=with_user,
        )

    def test_access_to_product_tag(self):
        logged_user = self.test_logged_user

        # internal user
        self._test_access_product_tag(allowed_ops="R", with_user=logged_user)

        # stock manager should not CUD
        logged_user.groups_id = [
            Command.link(self.env.ref("stock.group_stock_manager").id),
        ]
        self._test_access_product_tag(allowed_ops="R", with_user=logged_user)

        # with stock_settings_manager.group_stock_settings_manager should CRUD
        logged_user.groups_id = [
            Command.link(
                self.env.ref("stock_settings_manager.group_stock_settings_manager").id
            ),
        ]
        self._test_access_product_tag(allowed_ops="CRUD", with_user=logged_user)
