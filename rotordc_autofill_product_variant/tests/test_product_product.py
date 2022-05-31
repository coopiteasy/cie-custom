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
        default_code = "AAA"
        weight = 50.0
        product_length = 2.0
        product_width = 1.0
        product_height = 1.0
        self._set_value_on_product_tmpl(
            default_code=default_code,
            weight=weight,
            product_length=product_length,
            product_width=product_width,
            product_height=product_height,
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
            self.assertEqual(product.default_code, default_code)
            self.assertEqual(product.weight, weight)
            self.assertEqual(product.product_length, product_length)
            self.assertEqual(product.product_width, product_width)
            self.assertEqual(product.product_height, product_height)
