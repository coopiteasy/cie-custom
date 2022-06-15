# Copyright 2022 Coop IT Easy SCRL fs
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

import odoo.tests.common as common


class TestProductProduct(common.TransactionCase):
    def setUp(self):
        super().setUp()
        self.product_product_10 = self.env.ref("product.product_product_10")
        self.product_tmpl_10 = self.product_product_10.product_tmpl_id
        self.product_attribute_1 = self.env.ref("product.product_attribute_1")
        self.product_attribute_2 = self.env.ref("product.product_attribute_2")
        # Value for product_attribute_1
        self.product_attribute_value_11 = self.env.ref(
            "product.product_attribute_value_1"
        )
        self.product_attribute_value_12 = self.env.ref(
            "product.product_attribute_value_2"
        )
        # Value for product_attribute_2
        self.product_attribute_value_21 = self.env.ref(
            "product.product_attribute_value_3"
        )
        self.product_attribute_value_22 = self.env.ref(
            "product.product_attribute_value_4"
        )

        self.default_code = "AAA"
        self.weight = 50.0
        self.product_length = 2.0
        self.product_width = 1.0
        self.product_height = 1.0

    def _set_value_on_product_tmpl(
        self, default_code, weight, product_length, product_width, product_height
    ):
        self.product_tmpl_10.write(
            {
                "default_code": default_code,
                "weight": weight,
                "product_length": product_length,
                "product_width": product_width,
                "product_height": product_height,
            }
        )

    def test_autofill_when_creating_new_variant(self):
        self._set_value_on_product_tmpl(
            default_code=self.default_code,
            weight=self.weight,
            product_length=self.product_length,
            product_width=self.product_width,
            product_height=self.product_height,
        )
        self.product_tmpl_10.write(
            {
                "attribute_line_ids": [
                    [
                        0,
                        0,
                        {
                            "attribute_id": self.product_attribute_1.id,
                            "value_ids": [
                                [
                                    6,
                                    0,
                                    [
                                        self.product_attribute_value_11.id,
                                        self.product_attribute_value_12.id,
                                    ],
                                ]
                            ],
                        },
                    ],
                    [
                        0,
                        0,
                        {
                            "attribute_id": self.product_attribute_2.id,
                            "value_ids": [
                                [
                                    6,
                                    0,
                                    [
                                        self.product_attribute_value_21.id,
                                        self.product_attribute_value_22.id,
                                    ],
                                ]
                            ],
                        },
                    ],
                ]
            }
        )

        for product in self.product_tmpl_10.product_variant_ids:
            self.assertEqual(product.default_code, self.default_code)
            self.assertEqual(product.weight, self.weight)
            self.assertEqual(product.product_length, self.product_length)
            self.assertEqual(product.product_width, self.product_width)
            self.assertEqual(product.product_height, self.product_height)

    def test_autofill_for_new_template(self):
        product_template = self.env["product.template"].create(
            {
                "name": "New product",
                "default_code": self.default_code,
                "weight": self.weight,
                "product_length": self.product_length,
                "product_width": self.product_width,
                "product_height": self.product_height,
            }
        )
        for product in product_template.product_variant_ids:
            self.assertEqual(product.default_code, self.default_code)
            self.assertEqual(product.weight, self.weight)
            self.assertEqual(product.product_length, self.product_length)
            self.assertEqual(product.product_width, self.product_width)
            self.assertEqual(product.product_height, self.product_height)

        product_template.write(
            {
                "attribute_line_ids": [
                    [
                        0,
                        0,
                        {
                            "attribute_id": self.product_attribute_1.id,
                            "value_ids": [
                                [
                                    6,
                                    0,
                                    [
                                        self.product_attribute_value_11.id,
                                        self.product_attribute_value_12.id,
                                    ],
                                ]
                            ],
                        },
                    ],
                ]
            }
        )
        for product in product_template.product_variant_ids:
            self.assertEqual(product.default_code, self.default_code)
            self.assertEqual(product.weight, self.weight)
            self.assertEqual(product.product_length, self.product_length)
            self.assertEqual(product.product_width, self.product_width)
            self.assertEqual(product.product_height, self.product_height)
