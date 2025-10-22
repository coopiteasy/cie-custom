# Copyright (C) 2022-Today GRAP (http://www.grap.coop)
# @author Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    company_id = fields.Many2one(default=lambda x: x._default_company_id())

    def _default_company_id(self):
        if self.env.context.get("create_company", False):
            return False
        return self.env.company.id
