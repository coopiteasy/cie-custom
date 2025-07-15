# SPDX-FileCopyrightText: 2025 Coop IT Easy SC
#
# SPDX-License-Identifier: AGPL-3.0-or-later

from datetime import datetime

from odoo import Command
from odoo.exceptions import UserError
from odoo.tests import common


class TestDonationTaxReceipt(common.TransactionCase):
    def setUp(self, *args, **kwargs):
        super().setUp(*args, **kwargs)

        # Set up the environment
        self.env = self.env(
            context=dict(
                self.env.context,
                mail_create_nolog=True,
                mail_create_nosubscribe=True,
                mail_notrack=True,
                no_reset_password=True,
                tracking_disable=True,
            )
        )

        # Models
        self.company = self.env.ref("base.main_company")
        self.partner_donor = self.env.ref("donation_base.donor1")
        self.partner_donor2 = self.env.ref("donation_base.donor2")
        self.product_donation = self.env.ref("donation_base.product_product_donation")
        self.product_donation_no_tax = self.env.ref(
            "donation_base.product_product_donation_notaxreceipt"
        )
        self.DonationDonation = self.env["donation.donation"]
        self.DonationLine = self.env["donation.line"]
        self.DonationTaxReceipt = self.env["donation.tax.receipt"]

        # Create payment mode
        self.payment_mode = self.env.ref(
            "account_payment_mode.payment_mode_inbound_ct1"
        )
        self.bank_journal = self.env["account.journal"].create(
            {
                "type": "bank",
                "name": "test bank journal",
            }
        )
        self.payment_mode = self.env["account.payment.mode"].create(
            {
                "name": "test_payment_mode",
                "donation": True,
                "bank_account_link": "fixed",
                "fixed_journal_id": self.bank_journal.id,
                "payment_method_id": self.env.ref(
                    "account.account_payment_method_manual_in"
                ).id,
            }
        )

        self.product1 = self.env.ref("donation_base.product_product_donation")

    def test_create_tax_receipt(self):
        """
        Test that the tax receipt is correctly created and that it doesn't
        change on partner changes
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
        donation.write({"partner_id": self.partner_donor2})
        donation_tax_receipt = donation.tax_receipt_id
        self.assertEqual(donation_tax_receipt.street, self.partner_donor.street)
        self.assertEqual(donation_tax_receipt.street2, self.partner_donor.street2)
        self.assertEqual(donation_tax_receipt.city, self.partner_donor.city)
        self.assertEqual(donation_tax_receipt.state_id, self.partner_donor.state_id)
        self.assertEqual(donation_tax_receipt.zip, self.partner_donor.zip)
        self.assertEqual(donation_tax_receipt.country_id, self.partner_donor.country_id)

        self.assertNotEqual(donation_tax_receipt.street, self.partner_donor2.street)
        self.assertNotEqual(donation_tax_receipt.street2, self.partner_donor2.street2)
        self.assertNotEqual(donation_tax_receipt.city, self.partner_donor2.city)
        self.assertNotEqual(donation_tax_receipt.state_id, self.partner_donor2.state_id)
        self.assertNotEqual(donation_tax_receipt.zip, self.partner_donor2.zip)
        self.assertNotEqual(
            donation_tax_receipt.country_id, self.partner_donor2.country_id
        )

    def test_empty_address_raises_eror(self):
        donor_with_empty_address = self.env.ref("donation_base.donor2")
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
