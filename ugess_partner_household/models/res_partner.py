from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError
from odoo.tools.translate import _


class ResPartner(models.Model):
    _inherit = "res.partner"

    main_income_source_household = fields.Many2one(
        comodel_name="social.budget.move.category",
        string="Main Income Source of Household",
    )
    main_income_source_member = fields.Many2one(
        comodel_name="social.budget.move.category",
        string="Main Income Source of Member",
    )
    household_situation_id = fields.Many2one(
        comodel_name="household.situation",
        string="Household Situation",
        readonly=False,  # need to be able to edit it in partner form
    )
    household_member_ids = fields.One2many(
        comodel_name="household.member",
        inverse_name="partner_id",
        string="Family members",
        required=True,
    )
    linked_household_member_id = fields.Many2one(
        comodel_name="household.member",
        string="Self Represented As Household Member",
        compute="_compute_linked_household_member_id",
        store=True,
    )
    activate_household_functionality = fields.Boolean()

    number_of_persons_in_household = fields.Integer(
        string="Total number of persons in household",
        compute="_compute_number_of_persons_in_household",
        store=True,
    )
    number_of_babies_in_household = fields.Integer(
        string="Number of babies (0-3)",
        compute="_compute_number_of_persons_in_household",
        store=True,
    )
    number_of_children_in_household = fields.Integer(
        string="Number of children (3-14)",
        compute="_compute_number_of_persons_in_household",
        store=True,
    )
    number_of_adult_in_household = fields.Integer(
        string="Number of adults (>14)",
        compute="_compute_number_of_persons_in_household",
        store=True,
    )
    number_of_males_in_household = fields.Integer(
        string="Number of males",
        compute="_compute_number_of_persons_in_household",
        store=True,
    )
    number_of_females_in_household = fields.Integer(
        string="Number of females",
        compute="_compute_number_of_persons_in_household",
        store=True,
    )
    number_of_other_genders_in_household = fields.Integer(
        string="Number of persons of other genders",
        compute="_compute_number_of_persons_in_household",
        store=True,
    )
    number_of_unknown_genders_in_household = fields.Integer(
        string="Number of persons with unknown genders",
        compute="_compute_number_of_persons_in_household",
        store=True,
    )

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            # Create a linked household partner. We do this at creation time of
            # the partner instead of upon enabling the household functionality.
            # If we did it upon enabling the household functionality, we would
            # have to call `create` in an onchange method, which is not strictly
            # supported, and which leads to UI bugs.
            if not vals.get("household_member_ids"):
                vals.update(self._prepare_create_linked_member(vals))
        return super().create(vals_list)

    def write(self, vals):
        result = super().write(vals)
        for partner in self:
            member_vals = {}
            fields_to_sync = ["name", "job_position_id", "birthdate_date", "gender"]
            for field in fields_to_sync:
                field_value = vals.get(field)
                if field_value:
                    member_vals[field] = field_value
            # Exceptional case because the field names do not match.
            if "main_income_source_member" in vals:
                member_vals["main_income_source"] = vals["main_income_source_member"]
            # FIXME: This may break if linked_household_member_id is somehow
            # changed in this write action. This shouldn't be possible,
            # though.
            partner.linked_household_member_id.write(member_vals)
        return result

    @api.depends("household_member_ids")
    def _compute_linked_household_member_id(self):
        for partner in self:
            # The linked member (a representation of self) is always the first
            # member in the list.
            if partner.household_member_ids:
                partner.linked_household_member_id = partner.household_member_ids[0]
            else:
                partner.linked_household_member_id = False

    @api.depends("household_member_ids", "household_member_ids.age")
    def _compute_number_of_persons_in_household(self):
        for rec in self:
            members = self.env["household.member"].search([("partner_id", "=", rec.id)])
            rec.number_of_persons_in_household = len(members)
            rec.number_of_babies_in_household = len(
                members.filtered(lambda m: m.age <= 3)
            )
            rec.number_of_children_in_household = len(
                members.filtered(lambda m: m.age > 3 and m.age <= 14)
            )
            rec.number_of_adult_in_household = len(
                members.filtered(lambda m: m.age > 14)
            )
            rec.number_of_males_in_household = len(
                members.filtered(lambda m: m.gender == "male")
            )
            rec.number_of_females_in_household = len(
                members.filtered(lambda m: m.gender == "female")
            )
            rec.number_of_other_genders_in_household = len(
                members.filtered(lambda m: m.gender == "other")
            )
            rec.number_of_unknown_genders_in_household = len(
                members.filtered(lambda m: not m.gender)
            )

    @api.onchange("activate_household_functionality")
    def onchange_activate_household_functionality(self):
        self.ensure_one()
        if self.activate_household_functionality:
            # if self.id.origin is False (record does not yet exist in
            # database), we cannot proceed, because the linked member doesn't
            # exist yet.
            if not self.id.origin:
                # FIXME: Even though this is set back to False, the toggle in
                # the interface still shows it as enabled. I do not know why.
                # Fortunately, when clicking on 'Save', the toggle is reset to
                # disabled. This is exclusively a temporary visual bug.
                self.activate_household_functionality = False
                raise UserError(
                    _("Please save the partner before enabling the household.")
                )

    @api.constrains(
        "activate_household_functionality",
        "household_member_ids",
    )
    def _check_activate_household_functionality(self):
        for partner in self:
            if (
                partner.activate_household_functionality
                and not partner.household_member_ids
            ):
                raise ValidationError(
                    _("Partner %s must have at least one household member.")
                    % partner.name
                )

    @api.model
    def _prepare_create_linked_member(self, vals):
        return {
            "household_member_ids": [
                (
                    0,
                    False,
                    {
                        "name": vals.get("name"),
                        "job_position_id": vals.get("job_position_id"),
                        "main_income_source": vals.get("main_income_source_member"),
                        "birthdate_date": vals.get("birthdate_date"),
                        "gender": vals.get("gender"),
                    },
                )
            ]
        }

    def _create_linked_member(self):
        for partner in self:
            if not partner.household_member_ids:
                partner.write(
                    self._prepare_create_linked_member(
                        {
                            "name": partner.name,
                            "job_position_id": partner.job_position_id.id
                            if partner.job_position_id
                            else False,
                            "main_income_source": partner.main_income_source_member.id
                            if partner.main_income_source_member
                            else False,
                            "birthdate_date": partner.birthdate_date,
                            "gender": partner.gender,
                        }
                    )
                )
