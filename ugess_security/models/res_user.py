from odoo import api, models


class ResUsers(models.Model):
    _inherit = "res.users"

    @api.model
    def _default_role_lines(self):
        """This prevents any roles of the default user to be set on
        the just created user.
        We can refine this later on if needed"""
        return []
