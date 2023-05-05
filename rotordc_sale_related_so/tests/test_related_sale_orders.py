# Copyright 2023 Coop IT Easy SC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo.tests import SavepointCase


class TestRelatedSaleOrders(SavepointCase):
    @classmethod
    def setUpClass(cls):
        super(TestRelatedSaleOrders, cls).setUpClass()
        cls.sale_order_obj = cls.env["sale.order"]
        cls.customer = cls.env.ref("base.res_partner_1")
        cls.other_customer = cls.env.ref("base.res_partner_2")

    def _create_so(self, name, parent_so=None):
        vals = {
            "partner_id": self.customer.id,
            "name": name,
        }
        if parent_so:
            if not parent_so.sale_order_group_id:
                parent_so.sale_order_group_id = self.env["sale.order.group"].create({})
            vals["sale_order_group_id"] = parent_so.sale_order_group_id.id

        return self.sale_order_obj.create(vals)

    def test_discover_single_so(self):
        so = self._create_so("X")
        self.assertFalse(so.sale_order_group_id)
        self.assertFalse(so.related_so_ids)

    def test_discover_related_tree_for_sale_order_tree(self):
        """
        A ──► B ──► C
              │
              └───► D ──► E
        """
        A = self._create_so(name="A")
        B = self._create_so(name="B", parent_so=A)
        C = self._create_so(name="C", parent_so=B)
        D = self._create_so(name="D", parent_so=B)
        E = self._create_so(name="E", parent_so=D)

        self.assertEqual(sorted(A.related_so_ids.mapped("name")), list("BCDE"))
        self.assertEqual(sorted(B.related_so_ids.mapped("name")), list("ACDE"))
        self.assertEqual(sorted(C.related_so_ids.mapped("name")), list("ABDE"))
        self.assertEqual(sorted(D.related_so_ids.mapped("name")), list("ABCE"))
        self.assertEqual(sorted(E.related_so_ids.mapped("name")), list("ABCD"))
