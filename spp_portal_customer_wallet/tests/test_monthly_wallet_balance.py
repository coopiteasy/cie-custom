# SPDX-FileCopyrightText: 2023 Coop IT Easy SC
#
# SPDX-License-Identifier: AGPL-3.0-or-later

import datetime

from odoo.tests.common import SavepointCase


class TestMonthlyBalance(SavepointCase):
    @classmethod
    def setUpClass(cls, *args, **kwargs):
        super().setUpClass(*args, **kwargs)

        cls.partner_id = cls.env["res.partner"].create({"name": "Test Partner"})
        cls.customer_wallet_account = cls.env.ref(
            "account_customer_wallet.account_account_customer_wallet_demo"
        )
        cls.customer_wallet_journal = cls.env.ref(
            "account_customer_wallet.account_journal_customer_wallet_demo"
        )
        cls.cash_account = cls.env["account.account"].search(
            [("user_type_id.type", "=", "liquidity")], limit=1
        )

    def _create_move(self, debit=0, credit=0, date=None, partner=None):
        if partner is None:
            partner = self.partner_id
        if date is None:
            date = datetime.date.today()

        self.env["account.move"].create(
            {
                "journal_id": self.customer_wallet_journal.id,
                "date": date,
                "line_ids": [
                    (
                        0,
                        0,
                        {
                            "debit": debit,
                            "credit": credit,
                            "partner_id": partner.id,
                            "account_id": self.customer_wallet_account.id,
                        },
                    ),
                    (
                        0,
                        0,
                        {
                            "debit": credit,
                            "credit": debit,
                            "partner_id": partner.id,
                            "account_id": self.cash_account.id,
                        },
                    ),
                ],
            }
        )

    def test_credit_is_not_counted(self):
        """credit = increasing customer wallet budget. Not counted."""
        self._create_move(credit=100)
        self.assertFalse(self.partner_id.customer_wallet_payments_per_month())

    def test_one_payment(self):
        """Simple case."""
        self._create_move(debit=10, date=datetime.date(2023, 1, 1))
        result = self.partner_id.customer_wallet_payments_per_month()
        self.assertEqual(result[(2023, 1)], 10)

    def test_two_payments(self):
        """More complex case."""
        self._create_move(debit=10, date=datetime.date(2023, 1, 1))
        self._create_move(debit=5, date=datetime.date(2023, 1, 31))
        result = self.partner_id.customer_wallet_payments_per_month()
        self.assertEqual(result[(2023, 1)], 15)

    def test_multiple_months(self):
        """Separate months have separate keys."""
        self._create_move(debit=10, date=datetime.date(2023, 1, 1))
        self._create_move(debit=20, date=datetime.date(2023, 2, 1))
        result = self.partner_id.customer_wallet_payments_per_month()
        self.assertEqual(result[(2023, 1)], 10)
        self.assertEqual(result[(2023, 2)], 20)
        self.assertEqual(len(result), 2)

    def test_multiple_years(self):
        """Identical months in different years have separate keys."""
        self._create_move(debit=10, date=datetime.date(2023, 1, 1))
        self._create_move(debit=20, date=datetime.date(2024, 1, 1))
        result = self.partner_id.customer_wallet_payments_per_month()
        self.assertEqual(result[(2023, 1)], 10)
        self.assertEqual(result[(2024, 1)], 20)
