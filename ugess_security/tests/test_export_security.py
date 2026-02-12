from .common import CommonCase


class TestExportSecurity(CommonCase):
    def test_export_res_partner(self):
        groups = self._get_groups_with_perm_export("res.partner")
        self.assertItemsEqual(
            groups,
            [
                self.env.ref("ugess_security.role_ugess_social_res_groups"),
                self.env.ref("base.group_erp_manager"),
            ],
        )

    def test_export_product(self):
        groups = self._get_groups_with_perm_export("product.product")
        self.assertItemsEqual(
            groups,
            [
                self.env.ref("stock.group_stock_manager"),
            ],
        )
        groups = self._get_groups_with_perm_export("product.template")
        self.assertItemsEqual(
            groups,
            [
                self.env.ref("stock.group_stock_manager"),
            ],
        )

    def test_export_stock_move(self):
        groups = self._get_groups_with_perm_export("stock.move")
        self.assertItemsEqual(
            groups,
            [
                self.env.ref("stock.group_stock_manager"),
            ],
        )
        groups = self._get_groups_with_perm_export("stock.move.line")
        self.assertItemsEqual(
            groups,
            [
                self.env.ref("stock.group_stock_manager"),
            ],
        )

    def test_export_stock_quants(self):
        groups = self._get_groups_with_perm_export("stock.quant")
        self.assertItemsEqual(
            groups,
            [
                self.env.ref("stock.group_stock_manager"),
            ],
        )
