from odoo import Command

from .common import CommonCase


class TestStockSecurity(CommonCase):
    def _test_access_product_category(self, allowed_ops="CRUD", with_user=None):
        self._test_access_model(
            model_obj=self.env["product.category"],
            allowed_ops=allowed_ops,
            with_user=with_user,
        )

    def _test_access_supply_source(self, allowed_ops="CRUD", with_user=None):
        self._test_access_model(
            model_obj=self.env["supply.source"],
            allowed_ops=allowed_ops,
            with_user=with_user,
        )

    def _test_access_stock_quant_reason(self, allowed_ops="CRUD", with_user=None):
        self._test_access_model(
            model_obj=self.env["stock.quant.reason"],
            allowed_ops=allowed_ops,
            with_user=with_user,
        )

    def _test_access_scrap_reason_code(self, allowed_ops="CRUD", with_user=None):
        self._test_access_model(
            model_obj=self.env["scrap.reason.code"],
            allowed_ops=allowed_ops,
            with_user=with_user,
        )

    def test_access_to_product_category(self):
        logged_user = self.test_logged_user

        # internal user
        self._test_access_product_category(allowed_ops="R", with_user=logged_user)

        # with inventory admin right should not CUD on product_category
        logged_user.groups_id = [
            Command.link(self.env.ref("stock.group_stock_manager").id),
        ]
        self._test_access_product_category(allowed_ops="R", with_user=logged_user)

        # with inventory settings admin should CRUD
        logged_user.groups_id = [
            Command.link(
                self.env.ref("stock_settings_manager.group_stock_settings_manager").id
            ),
        ]
        self._test_access_product_category(allowed_ops="CRUD", with_user=logged_user)

    def test_access_to_supply_source(self):
        logged_user = self.test_logged_user

        # internal user
        self._test_access_supply_source(allowed_ops="R", with_user=logged_user)

        # with inventory admin right should not CUD on supply source
        logged_user.groups_id = [
            Command.link(self.env.ref("stock.group_stock_manager").id),
        ]
        self._test_access_supply_source(allowed_ops="R", with_user=logged_user)

        # with inventory settings admin should CRUD
        logged_user.groups_id = [
            Command.link(
                self.env.ref("stock_settings_manager.group_stock_settings_manager").id
            ),
        ]
        self._test_access_supply_source(allowed_ops="CRUD", with_user=logged_user)

    def test_access_stock_quant_reason(self):
        logged_user = self.test_logged_user

        # with inventory admin right should not CUD on stock quant reason
        logged_user.groups_id = [
            Command.link(self.env.ref("stock.group_stock_manager").id),
        ]
        self._test_access_stock_quant_reason(allowed_ops="R", with_user=logged_user)

        # with inventory settings admin should CRUD
        logged_user.groups_id = [
            Command.link(
                self.env.ref("stock_settings_manager.group_stock_settings_manager").id
            ),
        ]
        self._test_access_stock_quant_reason(allowed_ops="CRUD", with_user=logged_user)

    def test_access_scrap_reason_code(self):
        logged_user = self.test_logged_user

        # with inventory USER right should not U on scrap reason code
        logged_user.groups_id = [
            Command.link(self.env.ref("stock.group_stock_user").id),
        ]
        self._test_access_scrap_reason_code(allowed_ops="R", with_user=logged_user)

        # with inventory admin right should not CUD on scrap reason code
        logged_user.groups_id = [
            Command.link(self.env.ref("stock.group_stock_manager").id),
        ]
        self._test_access_scrap_reason_code(allowed_ops="R", with_user=logged_user)

        # with inventory settings admin should CRUD
        logged_user.groups_id = [
            Command.link(
                self.env.ref("stock_settings_manager.group_stock_settings_manager").id
            ),
        ]
        self._test_access_scrap_reason_code(allowed_ops="CRUD", with_user=logged_user)
