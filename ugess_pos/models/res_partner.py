# Copyright (C) 2022-Today GRAP (http://www.grap.coop)
# @author Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html


from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    household_text = fields.Char(
        compute="_compute_household_text",
        help="Technical field, used to display household information"
        " in the point of sale.",
    )

    @api.depends("household_member_ids.age")
    def _compute_household_text(self):
        """use of sudo() here because seeing this
        computed info is allowed to all users"""
        self_sudo = self.sudo()
        for partner in self_sudo.filtered(lambda x: x.household_member_ids):
            partner.household_text = "{} ({})".format(
                len(partner.sudo().household_member_ids),
                " / ".join(
                    [str(x) for x in sorted(partner.mapped("household_member_ids.age"))]
                ),
            )

        for partner in self_sudo.filtered(lambda x: not x.household_member_ids):
            partner.household_text = False
