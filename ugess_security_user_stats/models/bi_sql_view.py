# Copyright 2023 Akretion (http://www.akretion.com).
# @author Olivier Nibart <olivier.nibart@akretion.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models


class BiSQLView(models.Model):
    _inherit = "bi.sql.view"

    def _prepare_menu(self):
        res = super()._prepare_menu()
        anon_user_group = self.env.ref(
            "ugess_security_user_stats.role_ugess_anonymous_stats_user_res_groups",
            raise_if_not_found=False,
        )
        if anon_user_group and anon_user_group in self.group_ids:
            res.update(
                {
                    "parent_id": self.env.ref(
                        "ugess_security_user_stats.menu_bi_anon_sql_reports"
                    ).id,
                }
            )
        return res
