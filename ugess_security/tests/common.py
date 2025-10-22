from odoo.exceptions import AccessError
from odoo.tests import common

CRUD_OPS = {
    "C": "create",
    "R": "read",
    "U": "write",
    "D": "unlink",
}


class CommonCase(common.TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.test_logged_user = cls.env["res.users"].create(
            {
                "login": "john",
                "name": "John Doe",
                "groups_id": [(6, 0, [cls.env.ref("base.group_user").id])],
            }
        )

    def _test_access_model(
        self,
        model_obj,
        allowed_ops="CRUD",
        with_user=None,
    ):
        if with_user:
            model_obj = model_obj.with_user(with_user)

        for op, operation in CRUD_OPS.items():
            if op in allowed_ops:
                model_obj.check_access_rights(operation)
            else:
                with self.assertRaises(AccessError):
                    model_obj.check_access_rights(operation)

    def _test_complex_access_model(
        self,
        model_obj,
        search_domain,
        create_vals,
        write_vals,
        allowed_ops="CRUD",
        with_user=None,
    ):
        """this allows to test also the record rules when accessing models"""
        if with_user:
            model_obj = model_obj.with_user(with_user)

        def _do_op(op, new_obj):
            if op == "C":
                return model_obj.create(create_vals)
            elif op == "R":
                return model_obj.search(search_domain)
            elif op == "U":
                return new_obj.write(write_vals)
            elif op == "D":
                return new_obj.unlink()

        new_obj = None
        for op in "CRUD":
            if op in allowed_ops:
                res = _do_op(op, new_obj)
                if op == "R":
                    self.assertTrue(res)
                if op == "C":
                    new_obj = res.with_user(with_user) if with_user else res
            else:
                with self.assertRaises(AccessError):
                    _do_op(op, new_obj)
                # to have something to test UD
                if op == "C":
                    new_obj = model_obj.sudo().create(create_vals)
                    new_obj = new_obj.with_user(with_user) if with_user else new_obj

        # cleanup
        if new_obj and new_obj.exists():
            new_obj.sudo().unlink()

    def _get_groups_with_perm_export(self, model):
        model_access = self.env["ir.model.access"].search(
            [("model_id.model", "=", model), ("perm_export", "=", True)]
        )
        return model_access.mapped("group_id")
