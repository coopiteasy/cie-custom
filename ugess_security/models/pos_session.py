from odoo import models


class PosSession(models.Model):
    _inherit = "pos.session"

    # def get_closing_control_data(self):
    #   'is_manager': self.user_has_groups("point_of_sale.group_pos_manager"),

    def _get_pos_ui_hr_employee(self, params):
        """Users with 'UGESS grocer' role should be considered
        as manager on the UGESS POS"""
        employees = super()._get_pos_ui_hr_employee(params)
        user_ids = [
            employee["user_id"] for employee in employees if employee["user_id"]
        ]
        grocer_group_id = self.env.ref("ugess_security.role_ugess_grocer_res_groups")
        grocer_ids = (
            self.env["res.users"]
            .browse(user_ids)
            .filtered(lambda user: grocer_group_id in user.groups_id)
            .mapped("id")
        )
        for employee in employees:
            if (
                employee["role"] != "manager"
                and employee["user_id"]
                and employee["user_id"] in grocer_ids
            ):
                employee["role"] = "manager"

        return employees
