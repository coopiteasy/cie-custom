from odoo import _, models
from odoo.exceptions import AccessError


class ResPartner(models.Model):
    _inherit = "res.partner"

    def toggle_active(self):
        if not self.user_has_groups("ugess_security.group_res_partner_archive"):
            raise AccessError(
                _("You are not allowed to archive or unarchive a contact.")
            )
        super().toggle_active()
