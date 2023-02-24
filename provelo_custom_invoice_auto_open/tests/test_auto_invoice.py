# Copyright 2022 Coop IT Easy SC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

import odoo.tests.common as common


class TestAutoInvoice(common.SavepointCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.env = cls.env(context=dict(cls.env.context, tracking_disable=True))
        partner = cls.env.ref("base.res_partner_1")
        product = cls.env.ref("product.product_order_01")
        cls.user_demo = cls.env.ref("base.user_demo")

        so_vals = {
            "partner_id": partner.id,
            "order_line": [
                (
                    0,
                    0,
                    {
                        "product_id": product.id,
                    },
                )
            ],
        }
        cls.so = cls.env["sale.order"].sudo(cls.user_demo).create(so_vals)
        cls.so.action_confirm()

    def test_create_invoice_does_not_open_it_without_auto_invoice_group(self):
        invoice_id = self.so.action_invoice_create()
        invoice = self.env["account.invoice"].browse(invoice_id)
        self.assertEqual(invoice.state, "draft")

    def test_create_invoice_opens_it_for_auto_invoice_group(self):
        auto_invoice_group = self.env.ref(
            "provelo_custom_invoice_auto_open.account_invoice_auto_open_group"
        )
        self.user_demo.groups_id += auto_invoice_group
        invoice_id = self.so.action_invoice_create()
        invoice = self.env["account.invoice"].browse(invoice_id)
        self.assertEqual(invoice.state, "open")
