# pylint: disable=W8106

from odoo import api, fields, models
from odoo.exceptions import UserError
from odoo.tools.translate import _

from odoo.addons.partner_contact_birthdate.models.res_partner import (
    ResPartner as ResPartnerBirthdate,
)

# Propagating res.partner_fields to household.member
# using the metdhod in
# https://github.com/akretion/pos-sale-order/blob/
# 14.0/pos_sale_order/models/sale_order.py


class HouseholdMemberParent(models.Model):
    _name = "household.member"
    _description = "Household Member"


HouseholdMemberParent._compute_age = ResPartnerBirthdate._compute_age


class HouseholdMember(models.Model):
    _inherit = "household.member"

    name = fields.Char()

    is_active_member = fields.Boolean(string="Active Member", default=True)

    partner_id = fields.Many2one(
        "res.partner",
        string="Partner",
        ondelete="cascade",
        index=True,
        required=True,
        readonly=True,
    )
    is_linked_to_partner = fields.Boolean(
        string="Linked to Partner",
        compute="_compute_is_linked_to_partner",
    )
    job_position_id = fields.Many2one(
        "res.partner.job_position",
        "Professional Situation",
    )
    main_income_source = fields.Many2one(
        comodel_name="social.budget.move.category",
    )
    birthdate_date = fields.Date("Birthdate")
    # storing age to be able to use it in statistics
    # see the cron that will recompute it each day
    age = fields.Integer(readonly=True, compute="_compute_age", store=True)
    age_group = fields.Selection(
        [
            ("none", "None"),
            ("0-3", "0-3"),
            ("4-14", "4-14"),
            ("15-25", "15-25"),
            ("26-64", "26-64"),
            ("65+", "65+"),
        ],
        compute="_compute_age_group",
    )
    gender = fields.Selection(
        [("male", "Male"), ("female", "Female"), ("other", "Other")]
    )

    def unlink(self):
        raise UserError(_("Can not remove household member. Please archive it."))

    @api.depends(
        "partner_id",
        "partner_id.linked_household_member_id",
    )
    def _compute_is_linked_to_partner(self):
        for member in self:
            member.is_linked_to_partner = bool(
                member.partner_id.linked_household_member_id == member
            )

    @api.depends("birthdate_date", "age")
    def _compute_age_group(self):
        for rec in self:
            rec.age_group = self._convert_age_to_age_group(rec.age)

    @staticmethod
    def _convert_age_to_age_group(age):
        # Do not use "if not age" to not include age == 0
        if age is False or age is None:
            return "none"
        elif age <= 3:
            return "0-3"
        elif age <= 14:
            return "4-14"
        elif age <= 25:
            return "15-25"
        elif age <= 64:
            return "26-64"
        else:
            return "65+"

    @api.model
    def cron_compute_age(self):
        self.search([])._compute_age()

    @api.constrains("is_active_member")
    def _check_is_active_member(self):
        members = self.filtered(
            lambda x: not x.is_active_member and x.is_linked_to_partner
        )
        if members:
            raise UserError(
                _(
                    "Cannot archive household member '%s' because"
                    " it is linked to the partner."
                    " Please archive the partner instead."
                )
                % (",".join(members.mapped("name")))
            )
