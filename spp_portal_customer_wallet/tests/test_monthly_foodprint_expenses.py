# SPDX-FileCopyrightText: 2023 Coop IT Easy SC
#
# SPDX-License-Identifier: AGPL-3.0-or-later

import datetime

from .common import TestCommon


class TestMonthlyBalance(TestCommon):
    @classmethod
    def setUpClass(cls, *args, **kwargs):
        super().setUpClass(*args, **kwargs)

        cls.foodprint_product = cls.env["product.template"].create(
            {
                "name": "Test FoodPrint product",
                "is_foodprint_label": True,
            }
        )
        cls.foodprint_product_product = cls.foodprint_product.product_variant_id
        cls.regular_product = cls.env["product.template"].create(
            {
                "name": "Test regular product",
                "is_foodprint_label": False,
            }
        )
        cls.regular_product_product = cls.regular_product.product_variant_id

        cls.cash_account = cls.env["account.account"].create(
            {
                "name": "Test Cash Account",
                "code": "654321",
                "user_type_id": cls.env.ref("account.data_account_type_liquidity").id,
            }
        )
        cls.cash_journal = cls.env["account.journal"].create(
            {
                "name": "Test Cash Journal",
                "code": "CASH",
                "type": "cash",
                "journal_user": True,
                "default_debit_account_id": cls.cash_account.id,
                "default_credit_account_id": cls.cash_account.id,
            }
        )
        cls.pos_config = cls.env.ref("point_of_sale.pos_config_main")
        cls.pos_config.journal_ids += cls.customer_wallet_journal
        cls.pos_config.journal_ids += cls.cash_journal

        cls.pos_session = cls.env["pos.session"].create(
            {"user_id": 1, "config_id": cls.pos_config.id}
        )

        cls.wallet_statement = cls.pos_session.statement_ids.filtered(
            lambda x: x.journal_id == cls.customer_wallet_journal
        )
        cls.cash_statement = cls.pos_session.statement_ids.filtered(
            lambda x: x.journal_id == cls.cash_journal
        )

    def setUp(self, *args, **kwargs):
        super().setUp(*args, **kwargs)

        self._create_move(credit=100)

    def test_one_payment(self):
        order_data = [
            {
                "id": "0006-001-0010",
                "to_invoice": False,
                "data": {
                    "creation_date": "2023-01-01 12:00:00",
                    "name": "Order 0006-001-0010",
                    "uid": "00001-001-0001",
                    "pricelist_id": self.pricelist_id.id,
                    "user_id": 1,
                    "partner_id": self.partner_id.id,
                    "fiscal_position_id": False,
                    "sequence_number": 1,
                    "amount_tax": 0,
                    "amount_return": 0,
                    "amount_total": 10.0,
                    "amount_paid": 10,
                    "pos_session_id": self.pos_session.id,
                    "lines": [
                        [
                            0,
                            0,
                            {
                                "product_id": self.foodprint_product_product.id,
                                "price_unit": 10,
                                "qty": 1,
                                "price_subtotal": 10.0,
                                "price_subtotal_incl": 10.0,
                                "tax_ids": False,
                            },
                        ]
                    ],
                    "statement_ids": [
                        [
                            0,
                            0,
                            {
                                "journal_id": self.customer_wallet_journal.id,
                                "amount": 10.0,
                                "name": datetime.datetime(2023, 1, 1),
                                "account_id": self.customer_wallet_account.id,
                                "statement_id": self.wallet_statement.id,
                            },
                        ]
                    ],
                },
            }
        ]

        self.env["pos.order"].create_from_ui(order_data)

        self.pos_session.action_pos_session_closing_control()

        result = self.partner_id.foodprint_payments_per_month()
        self.assertEqual(result[(2023, 1)], 10)

    def test_two_products(self):
        order_data = [
            {
                "id": "0006-001-0010",
                "to_invoice": False,
                "data": {
                    "creation_date": "2023-01-01 12:00:00",
                    "name": "Order 0006-001-0010",
                    "uid": "00001-001-0001",
                    "pricelist_id": self.pricelist_id.id,
                    "user_id": 1,
                    "partner_id": self.partner_id.id,
                    "fiscal_position_id": False,
                    "sequence_number": 1,
                    "amount_tax": 0,
                    "amount_return": 0,
                    "amount_total": 20.0,
                    "amount_paid": 20,
                    "pos_session_id": self.pos_session.id,
                    "lines": [
                        [
                            0,
                            0,
                            {
                                "product_id": self.foodprint_product_product.id,
                                "price_unit": 10,
                                "qty": 1,
                                "price_subtotal": 10.0,
                                "price_subtotal_incl": 10.0,
                                "tax_ids": False,
                            },
                        ],
                        [
                            0,
                            0,
                            {
                                "product_id": self.regular_product_product.id,
                                "price_unit": 10,
                                "qty": 1,
                                "price_subtotal": 10.0,
                                "price_subtotal_incl": 10.0,
                                "tax_ids": False,
                            },
                        ],
                    ],
                    "statement_ids": [
                        [
                            0,
                            0,
                            {
                                "journal_id": self.customer_wallet_journal.id,
                                "amount": 20.0,
                                "name": datetime.datetime(2023, 1, 1),
                                "account_id": self.customer_wallet_account.id,
                                "statement_id": self.wallet_statement.id,
                            },
                        ]
                    ],
                },
            }
        ]

        self.env["pos.order"].create_from_ui(order_data)

        self.pos_session.action_pos_session_closing_control()

        result = self.partner_id.foodprint_payments_per_month()
        self.assertEqual(result[(2023, 1)], 10)

    def test_two_months(self):
        order_data = [
            {
                "id": "0006-001-0010",
                "to_invoice": False,
                "data": {
                    "creation_date": "2023-01-01 12:00:00",
                    "name": "Order 0006-001-0010",
                    "uid": "00001-001-0001",
                    "pricelist_id": self.pricelist_id.id,
                    "user_id": 1,
                    "partner_id": self.partner_id.id,
                    "fiscal_position_id": False,
                    "sequence_number": 1,
                    "amount_tax": 0,
                    "amount_return": 0,
                    "amount_total": 10.0,
                    "amount_paid": 10,
                    "pos_session_id": self.pos_session.id,
                    "lines": [
                        [
                            0,
                            0,
                            {
                                "product_id": self.foodprint_product_product.id,
                                "price_unit": 10,
                                "qty": 1,
                                "price_subtotal": 10.0,
                                "price_subtotal_incl": 10.0,
                                "tax_ids": False,
                            },
                        ],
                    ],
                    "statement_ids": [
                        [
                            0,
                            0,
                            {
                                "journal_id": self.customer_wallet_journal.id,
                                "amount": 10.0,
                                "name": datetime.datetime(2023, 1, 1),
                                "account_id": self.customer_wallet_account.id,
                                "statement_id": self.wallet_statement.id,
                            },
                        ]
                    ],
                },
            },
            {
                "id": "0006-001-0011",
                "to_invoice": False,
                "data": {
                    "creation_date": "2023-02-01 12:00:00",
                    "name": "Order 0006-001-0011",
                    "uid": "00001-001-0002",
                    "pricelist_id": self.pricelist_id.id,
                    "user_id": 1,
                    "partner_id": self.partner_id.id,
                    "fiscal_position_id": False,
                    "sequence_number": 1,
                    "amount_tax": 0,
                    "amount_return": 0,
                    "amount_total": 10.0,
                    "amount_paid": 10,
                    "pos_session_id": self.pos_session.id,
                    "lines": [
                        [
                            0,
                            0,
                            {
                                "product_id": self.foodprint_product_product.id,
                                "price_unit": 10,
                                "qty": 1,
                                "price_subtotal": 10.0,
                                "price_subtotal_incl": 10.0,
                                "tax_ids": False,
                            },
                        ],
                    ],
                    "statement_ids": [
                        [
                            0,
                            0,
                            {
                                "journal_id": self.customer_wallet_journal.id,
                                "amount": 10.0,
                                "name": datetime.datetime(2023, 2, 1),
                                "account_id": self.customer_wallet_account.id,
                                "statement_id": self.wallet_statement.id,
                            },
                        ]
                    ],
                },
            },
        ]

        self.env["pos.order"].create_from_ui(order_data)

        self.pos_session.action_pos_session_closing_control()

        result = self.partner_id.foodprint_payments_per_month()
        self.assertEqual(result[(2023, 1)], 10)
        self.assertEqual(result[(2023, 2)], 10)
        self.assertEqual(len(result), 2)

    def test_paid_with_cash(self):
        order_data = [
            {
                "id": "0006-001-0010",
                "to_invoice": False,
                "data": {
                    "creation_date": "2023-01-01 12:00:00",
                    "name": "Order 0006-001-0010",
                    "uid": "00001-001-0001",
                    "pricelist_id": self.pricelist_id.id,
                    "user_id": 1,
                    "partner_id": self.partner_id.id,
                    "fiscal_position_id": False,
                    "sequence_number": 1,
                    "amount_tax": 0,
                    "amount_return": 0,
                    "amount_total": 10.0,
                    "amount_paid": 10,
                    "pos_session_id": self.pos_session.id,
                    "lines": [
                        [
                            0,
                            0,
                            {
                                "product_id": self.foodprint_product_product.id,
                                "price_unit": 10,
                                "qty": 1,
                                "price_subtotal": 10.0,
                                "price_subtotal_incl": 10.0,
                                "tax_ids": False,
                            },
                        ]
                    ],
                    "statement_ids": [
                        [
                            0,
                            0,
                            {
                                "journal_id": self.cash_journal.id,
                                "amount": 10.0,
                                "name": datetime.datetime(2023, 1, 1),
                                "account_id": self.cash_account.id,
                                "statement_id": self.cash_statement.id,
                            },
                        ]
                    ],
                },
            }
        ]

        self.env["pos.order"].create_from_ui(order_data)

        self.pos_session.action_pos_session_closing_control()

        result = self.partner_id.foodprint_payments_per_month()
        self.assertEqual(len(result), 0)
