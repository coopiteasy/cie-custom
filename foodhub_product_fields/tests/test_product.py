# SPDX-FileCopyrightText: 2022 Coop IT Easy SC
#
# SPDX-License-Identifier: AGPL-3.0-or-later

from odoo.tests.common import TransactionCase


class TestProduct(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.hs_code = cls.env["hs.code"].create(
            {
                "local_code": "12345678",
                "description": "test",
            }
        )
        cls.supplier = cls.env["res.partner"].create(
            {
                "name": "Supplier",
            }
        )
        cls.product = cls.env["product.template"].create(
            {
                "name": "Test Product",
                "volume": 4,
                "weight": 2,
                "seller_ids": [
                    (0, 0, {"partner_id": cls.supplier.id}),
                ],
                "default_code": "123",
                "hs_code_id": cls.hs_code.id,
                "origin_country_id": cls.env.ref("base.be").id,
            }
        )

    def test_copy_product(self):
        """When copying a product, the relevant fields are also copied."""
        new_product = self.product.copy()
        self.assertEqual(new_product.volume, self.product.volume)
        self.assertEqual(new_product.weight, self.product.weight)
        self.assertEqual(new_product.seller_ids[0].partner_id.name, self.supplier.name)
        self.assertEqual(new_product.hs_code_id, self.product.hs_code_id)
        self.assertEqual(new_product.default_code, self.product.default_code)
        self.assertEqual(new_product.origin_country_id, self.product.origin_country_id)
