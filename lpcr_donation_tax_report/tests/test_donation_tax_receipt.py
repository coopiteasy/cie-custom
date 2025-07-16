# SPDX-FileCopyrightText: 2025 Coop IT Easy SC
#
# SPDX-License-Identifier: AGPL-3.0-or-later

from datetime import datetime

from odoo import Command
from odoo.exceptions import UserError
from odoo.tests.common import TransactionCase


class TestDonationTaxReceipt(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        # Set up the environment
        cls.env = cls.env(
            context=dict(
                cls.env.context,
                mail_create_nolog=True,
                mail_create_nosubscribe=True,
                mail_notrack=True,
                no_reset_password=True,
                tracking_disable=True,
            )
        )

        # Models
        cls.company = cls.env.ref("base.main_company")
        cls.partner_donor = cls.env.ref("donation_base.donor1")
        cls.partner_donor.street2 = "donor1 dummy street2 value"
        dummy_state1 = cls.env["res.country.state"].create(
            {
                "country_id": cls.env.ref("base.fr").id,
                "name": "dummy state 1",
                "code": "ds1",
            }
        )
        cls.partner_donor.state_id = dummy_state1
        cls.partner_donor2 = cls.env.ref("donation_base.donor2")
        cls.partner_donor2.street2 = "donor2 dummy street2 value"
        dummy_state2 = cls.env["res.country.state"].create(
            {
                "country_id": cls.env.ref("base.be").id,
                "name": "dummy state 2",
                "code": "ds2",
            }
        )
        cls.partner_donor2.country_id = cls.env.ref("base.be")
        cls.partner_donor2.state_id = dummy_state2
        cls.product_donation = cls.env.ref("donation_base.product_product_donation")
        cls.product_donation_no_tax = cls.env.ref(
            "donation_base.product_product_donation_notaxreceipt"
        )
        cls.DonationDonation = cls.env["donation.donation"]
        cls.DonationLine = cls.env["donation.line"]
        cls.DonationTaxReceipt = cls.env["donation.tax.receipt"]

        # Create payment mode
        cls.payment_mode = cls.env.ref("account_payment_mode.payment_mode_inbound_ct1")
        cls.bank_journal = cls.env["account.journal"].create(
            {
                "type": "bank",
                "name": "test bank journal",
            }
        )
        cls.payment_mode = cls.env["account.payment.mode"].create(
            {
                "name": "test_payment_mode",
                "donation": True,
                "bank_account_link": "fixed",
                "fixed_journal_id": cls.bank_journal.id,
                "payment_method_id": cls.env.ref(
                    "account.account_payment_method_manual_in"
                ).id,
            }
        )

        cls.product1 = cls.env.ref("donation_base.product_product_donation")

    def test_create_tax_receipt(self):
        """
        Test that the tax receipt is correctly created and that it doesn't
        change when the partner's values change
        """
        donation = self.DonationDonation.create(
            {
                "donation_date": datetime(2023, 1, 1),
                "partner_id": self.partner_donor.id,
                "company_id": self.company.id,
                "state": "draft",
                "payment_mode_id": self.payment_mode.id,
                "line_ids": [
                    Command.create(
                        {
                            "product_id": self.product1.id,
                            "quantity": 1,
                            "unit_price": 100.0,
                        }
                    ),
                ],
            }
        )

        donation.validate()
        # the donation should store the partner's values at the time of
        # creation.
        fields = [
            "name",
            "email",
            "street",
            "street2",
            "city",
            "state_id",
            "zip",
            "country_id",
        ]
        current_values = {field: self.partner_donor[field] for field in fields}
        new_values = {field: self.partner_donor2[field] for field in fields}
        self.partner_donor.write(new_values)
        donation_tax_receipt = donation.tax_receipt_id
        self.assertEqual(donation_tax_receipt.donor_name, current_values["name"])
        self.assertEqual(donation_tax_receipt.street, current_values["street"])
        self.assertEqual(donation_tax_receipt.street2, current_values["street2"])
        self.assertEqual(donation_tax_receipt.city, current_values["city"])
        self.assertEqual(donation_tax_receipt.state_id, current_values["state_id"])
        self.assertEqual(donation_tax_receipt.zip, current_values["zip"])
        self.assertEqual(donation_tax_receipt.country_id, current_values["country_id"])

        self.assertNotEqual(donation_tax_receipt.donor_name, new_values["name"])
        self.assertNotEqual(donation_tax_receipt.street, new_values["street"])
        self.assertNotEqual(donation_tax_receipt.street2, new_values["street2"])
        self.assertNotEqual(donation_tax_receipt.city, new_values["city"])
        self.assertNotEqual(donation_tax_receipt.state_id, new_values["state_id"])
        self.assertNotEqual(donation_tax_receipt.zip, new_values["zip"])
        self.assertNotEqual(donation_tax_receipt.country_id, new_values["country_id"])

        # email is the exception: it should update with the partner's
        self.assertNotEqual(donation_tax_receipt.email, current_values["email"])
        self.assertEqual(donation_tax_receipt.email, new_values["email"])

    def test_empty_address_raises_eror(self):
        donor_with_empty_address = self.partner_donor2
        donor_with_empty_address.street = False
        donation = self.DonationDonation.create(
            {
                "donation_date": datetime(2023, 1, 1),
                "partner_id": donor_with_empty_address.id,
                "company_id": self.company.id,
                "state": "draft",
                "payment_mode_id": self.payment_mode.id,
                "tax_receipt_option": "each",
                "line_ids": [
                    Command.create(
                        {
                            "product_id": self.product1.id,
                            "quantity": 1,
                            "unit_price": 100.0,
                        }
                    ),
                ],
            }
        )
        with self.assertRaises(UserError):
            donation.validate()

        donor_with_empty_address.street = "not empty anymore"
        donation.validate()
