# SPDX-FileCopyrightText: 2023 Coop IT Easy SC
#
# SPDX-License-Identifier: AGPL-3.0-or-later

from odoo.exceptions import UserError
from odoo.tests.common import TransactionCase


class TestProductPrintCategory(TransactionCase):
    """Tests for 'Product Print Category' Module"""

    def setUp(self):
        super().setUp()
        self.supplier1 = self.env["res.partner"].create({"name": "Supplier 1"})
        self.supplier2 = self.env["res.partner"].create({"name": "Supplier 2"})
        self.supplier3 = self.env["res.partner"].create({"name": "Supplier 3"})
        self.product1 = self.env["product.product"].create({"name": "Test product 1"})
        self.product2 = self.env["product.product"].create({"name": "Test product 2"})
        self.po1 = self.env["purchase.order"].create(
            {
                "partner_id": self.supplier1.id,
                "state": "draft",
                "order_line": [
                    (0, 0, {"product_id": self.product1.id, "product_qty": 3}),
                    (0, 0, {"product_id": self.product2.id, "product_qty": 5}),
                ],
            }
        )
        self.po2 = self.env["purchase.order"].create(
            {
                "partner_id": self.supplier1.id,
                "state": "purchase",
                "order_line": [
                    (0, 0, {"product_id": self.product1.id, "product_qty": 10}),
                    (0, 0, {"product_id": self.product2.id, "product_qty": 5}),
                ],
                "date_approve": "2023-01-01",
            }
        )
        self.po3 = self.env["purchase.order"].create(
            {
                "partner_id": self.supplier1.id,
                "state": "purchase",
                "order_line": [
                    (0, 0, {"product_id": self.product1.id, "product_qty": 2}),
                    (0, 0, {"product_id": self.product2.id, "product_qty": 5}),
                ],
                "date_approve": "2023-04-01",
            }
        )
        self.po4 = self.env["purchase.order"].create(
            {
                "partner_id": self.supplier2.id,
                "state": "done",
                "order_line": [
                    (0, 0, {"product_id": self.product1.id, "product_qty": 10}),
                    (0, 0, {"product_id": self.product2.id, "product_qty": 15}),
                ],
                "date_approve": "2023-04-05",
            }
        )
        self.po5 = self.env["purchase.order"].create(
            {
                "partner_id": self.supplier3.id,
                "state": "cancel",
                "order_line": [
                    (0, 0, {"product_id": self.product1.id, "product_qty": 1}),
                    (0, 0, {"product_id": self.product2.id, "product_qty": 15}),
                ],
                "date_approve": "2023-04-10",
            }
        )

    def test_01_supplier_certificate_generator(self):
        """Test that a certificate with no matching purchase order is empty"""
        certificate_generator = self.env["bao.supplier.certificate.generator"].create(
            {
                "name": "Certificate - march 2023",
                "start_date": "2023-03-01",
                "end_date": "2023-03-31",
            }
        )
        self.assertEqual(certificate_generator.state, "draft")
        certificate_generator.action_confirm()
        self.assertTrue(self.supplier1 not in certificate_generator.supplier_ids)
        self.assertTrue(self.supplier2 not in certificate_generator.supplier_ids)
        self.assertTrue(self.supplier3 not in certificate_generator.supplier_ids)
        self.assertEqual(len(certificate_generator.supplier_ids), 0)
        self.assertEqual(len(certificate_generator.supplier_certificate_ids), 0)

    def test_02_supplier_certificate_generator(self):
        """Test that a certificate with matching purchase order is correct"""
        certificate_generator = self.env["bao.supplier.certificate.generator"].create(
            {
                "name": "Certificate - april 2023",
                "start_date": "2023-04-01",
                "end_date": "2023-04-30",
            }
        )
        self.assertEqual(certificate_generator.state, "draft")
        certificate_generator.action_confirm()
        self.assertTrue(self.supplier1 in certificate_generator.supplier_ids)
        self.assertTrue(self.supplier2 in certificate_generator.supplier_ids)
        self.assertTrue(self.supplier3 not in certificate_generator.supplier_ids)
        self.assertEqual(len(certificate_generator.supplier_ids), 2)
        self.assertEqual(len(certificate_generator.supplier_certificate_ids), 2)
        certificate_generator.action_send_email()
        self.assertTrue(certificate_generator.sent)
        self.assertRaises(UserError, certificate_generator.action_cancel)
