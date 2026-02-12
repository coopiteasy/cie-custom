# SPDX-FileCopyrightText: 2022 Coop IT Easy SC
#
# SPDX-License-Identifier: AGPL-3.0-or-later

from freezegun import freeze_time

from odoo import fields

from .common import UgessMembershipCommon


class TestPricelist(UgessMembershipCommon):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.pricelist_id = cls.env["product.pricelist"].create(
            {
                "name": "Test Pricelist",
            }
        )
        cls.membership_template_id.membership_pricelist_id = cls.pricelist_id

        cls.other_pricelist_id = cls.env["product.pricelist"].create(
            {
                "name": "Other Test Pricelist",
            }
        )
        cls.other_membership_template_id = cls.env["product.template"].create(
            {
                "name": "Other Test Membership",
                "membership_type": "custom",
                "membership_pricelist_id": cls.other_pricelist_id.id,
            }
        )
        cls.other_membership_id = cls.other_membership_template_id.product_variant_id

    @freeze_time("2022-02-04")
    def test_partner_simple_pricelist(self):
        self.assertEqual(
            self.partner_id.property_product_pricelist,
            self.pricelist_id,
        )

    @freeze_time("2022-05-04")
    def test_partner_pricelist_later_membership(self):
        """The membership with the later start date takes precedence."""
        self.env["membership.membership_line"].create(
            {
                "membership_id": self.other_membership_id.id,
                "partner": self.partner_id.id,
                "member_price": 1,
                "date_from": fields.date(2022, 5, 1),
                "date_to": fields.date(2023, 5, 1),
                "state": "paid",
            }
        )
        self.assertEqual(
            self.partner_id.property_product_pricelist,
            self.other_pricelist_id,
        )
