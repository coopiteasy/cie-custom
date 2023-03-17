# SPDX-FileCopyrightText: 2023 Coop IT Easy SC
#
# SPDX-License-Identifier: AGPL-3.0-or-later

import datetime

from odoo.tests.common import SavepointCase


class TestCommon(SavepointCase):
    @classmethod
    def setUpClass(cls, *args, **kwargs):
        super().setUpClass(*args, **kwargs)

        cls.partner_id = cls.env["res.partner"].create({"name": "Test Partner"})
        cls.company_id = cls.env.ref("base.main_company")
        cls.pricelist_id = cls.partner_id.property_product_pricelist
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
