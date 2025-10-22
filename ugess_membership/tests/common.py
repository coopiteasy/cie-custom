# SPDX-FileCopyrightText: 2022 Coop IT Easy SC
#
# SPDX-License-Identifier: AGPL-3.0-or-later

from odoo import fields
from odoo.tests.common import TransactionCase


class UgessMembershipCommon(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.partner_id = cls.env["res.partner"].create(
            {
                "name": "Jane Doe",
            }
        )
        cls.membership_template_id = cls.env["product.template"].create(
            {
                "name": "Test Membership",
                "membership_type": "custom",
                "membership": True,
            }
        )
        cls.membership_id = cls.membership_template_id.product_variant_id
        cls.membership_line_id = cls.env["membership.membership_line"].create(
            {
                "membership_id": cls.membership_id.id,
                "partner": cls.partner_id.id,
                "member_price": 1,
                "state": "paid",
                # 2022-02-03 is a Thursday
                "date_from": fields.date(2022, 2, 3),
                "date_to": fields.date(2023, 2, 3),
                "expenditure_ceiling": 100,
                "expenditure_ceiling_period": "week",
            }
        )

    def _create_expenditure_override(
        self,
        date_from,
        date_to,
        membership_line_id=None,
        expenditure_ceiling=50,
    ):
        if membership_line_id is None:
            membership_line_id = self.membership_line_id
        return self.env["membership.membership_line.expenditure.override"].create(
            {
                "membership_line_id": membership_line_id.id,
                "date_from": date_from,
                "date_to": date_to,
                "expenditure_ceiling": expenditure_ceiling,
            }
        )
