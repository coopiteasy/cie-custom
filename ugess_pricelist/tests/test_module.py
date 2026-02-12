# SPDX-FileCopyrightText: 2022 Coop IT Easy SC
#
# SPDX-License-Identifier: AGPL-3.0-or-later

from odoo.tests.common import TransactionCase


class TestModule(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.product_with_prices = cls.env.ref(
            "ugess_pricelist.demo_product_with_specific_prices"
        )
        cls.product_without_prices = cls.env.ref(
            "ugess_pricelist.demo_product_without_prices"
        )

    def test_prices_defined(self):
        self.assertEqual(
            self.product_with_prices.ugess_beneficiary_price,
            self.env.ref("ugess_pricelist.pricelist_item_beneficiary").fixed_price,
        )

        self.assertEqual(
            self.product_with_prices.ugess_solidary_price,
            self.env.ref("ugess_pricelist.pricelist_item_solidary").fixed_price,
        )

        self.assertEqual(
            self.product_with_prices.ugess_average_market_price,
            self.env.ref("ugess_pricelist.pricelist_item_average_market").fixed_price,
        )

    def test_prices_undefined(self):
        self.assertEqual(
            self.product_without_prices.ugess_beneficiary_price,
            0.0,
        )

        self.assertEqual(
            self.product_without_prices.ugess_solidary_price,
            0.0,
        )

        self.assertEqual(
            self.product_without_prices.ugess_average_market_price,
            0.0,
        )
