# SPDX-FileCopyrightText: 2026 Coop IT Easy SC
#
# SPDX-License-Identifier: AGPL-3.0-or-later

from odoo import api, fields, models
from odoo.osv.expression import SQL_OPERATORS
from odoo.tools.sql import SQL


class ResPartner(models.Model):
    _inherit = "res.partner"

    social_type = fields.Selection(
        [
            ("accompagner", "Accompagner"),
            ("beneficiary", "Beneficiary"),
            ("partner", "Partner"),
            ("other", "Other"),
        ],
        default="beneficiary",
    )
    is_social_benefactor = fields.Boolean("Benefactor")
    is_social_volunteer = fields.Boolean("Volunteer")

    social_beneficiary_ids = fields.Many2many(
        "res.partner",
        "beneficiary_partner_rel",
        "social_partner",
        "social_beneficiary",
        string="Beneficiaries",
        domain=[("social_type", "=", "beneficiary")],
    )
    social_partner_ids = fields.Many2many(
        "res.partner",
        "beneficiary_partner_rel",
        "social_beneficiary",
        "social_partner",
        string="Partners",
        domain=[("social_type", "=", "partner")],
    )

    social_file_creation_date = fields.Date(
        string="File Creation Date",
        required=True,
        default=fields.Date.context_today,
    )

    national_register_number = fields.Text()

    # Beneficiary
    social_beneficiary_orientation_id = fields.Many2one(
        "partner.social.orientation",
        string="Orientation",
    )
    social_beneficiary_gdpr = fields.Boolean(string="GDPR")
    social_beneficiary_spoken_language = fields.Char(string="Spoken Language")
    social_beneficiary_residence_permit_title_id = fields.Many2one(
        "partner.social.residence.permit.title",
        string="Residence Permit Title",
    )
    social_beneficiary_contact_person_name = fields.Char(string="Contact Person Name")
    social_beneficiary_contact_person_mobile = fields.Char(
        string="Contact Person Mobile"
    )
    social_beneficiary_civil_status_id = fields.Many2one(
        "partner.social.civil.status",
        string="Civil Status",
    )
    social_beneficiary_children_count = fields.Integer(string="Children Count")
    social_beneficiary_household_type_id = fields.Many2one(
        "partner.social.household.type",
        string="Household Type",
    )
    social_beneficiary_resource_ids = fields.Many2many(
        "partner.social.resource",
        string="Resource",
    )
    social_beneficiary_belgium_since_date = fields.Date(string="In Belgium Since")
    social_beneficiary_residence_right_id = fields.Many2one(
        "partner.social.residence.right",
        string="Residence Right",
    )

    # Volunteer
    social_volunteer_professional_status_id = fields.Many2one(
        "partner.social.volunteer.professional.status",
        string="Professional Status",
    )
    social_volunteer_personal_email = fields.Char(string="Personal Email")
    social_volunteer_nationality_country_id = fields.Many2one(
        "res.country",
        string="Nationality",
    )
    social_volunteer_contact_method_id = fields.Many2one(
        "partner.social.volunteer.contact.method",
        string="Contact Method",
    )
    social_volunteer_course_ids = fields.One2many(
        "partner.social.volunteer.course",
        "partner_id",
        string="Volunteer Course",
    )
    social_volunteer_type_ids = fields.Many2many(
        "partner.social.volunteer.type",
        "partner_social_volunteer_type_rel",
        "partner_id",
        "volunteer_type_id",
        string="Volunteer Types",
    )
    social_volunteer_motivation_ids = fields.Many2many(
        "partner.social.volunteer.motivation",
        "partner_social_volunteer_motivation_rel",
        "partner_id",
        "motivation_id",
        string="Motivations",
    )

    # Partner
    social_partner_structure_id = fields.Many2one(
        "partner.social.structure",
        string="Structure",
    )

    # The logic on properties used here follows the one done in
    # oca/partner-contact/partner_property
    # The properties are defined on the company
    social_properties_company_id = fields.Many2one(
        compute="_compute_social_properties_company_id",
        search="_search_social_properties_company_id",
        comodel_name="res.company",
    )

    social_beneficiary_properties = fields.Properties(
        definition="social_properties_company_id.partner_properties_definition_social_beneficiary"
    )
    social_volunteer_properties = fields.Properties(
        definition="social_properties_company_id.partner_properties_definition_social_volunteer"
    )
    social_partner_properties = fields.Properties(
        definition="social_properties_company_id.partner_properties_definition_social_partner"
    )
    social_benefactor_properties = fields.Properties(
        definition="social_properties_company_id.partner_properties_definition_social_benefactor"
    )

    @api.depends("company_id")
    @api.depends_context("company")
    def _compute_social_properties_company_id(self):
        for item in self:
            item.social_properties_company_id = item.company_id or self.env.company

    def _search_social_properties_company_id(self, operator, value):
        self.flush_model(["company_id"])
        query = self._where_calc([])
        query.add_where(
            SQL(
                "%s %s %s",
                self._field_to_sql(self._table, "social_properties_company_id", query),
                SQL_OPERATORS[operator],
                value,
            )
        )
        return [("id", "in", query)]

    def _field_to_sql(self, alias, fname, query=None, flush: bool = True) -> SQL:
        # OVERRIDE to allow to export the properties
        if fname == "social_properties_company_id":
            return SQL(
                """COALESCE(%(company_column)s, %(env_company)s)""",
                company_column=SQL.identifier(alias, "company_id"),
                env_company=self.env.company.id,
            )
        return super()._field_to_sql(alias, fname, query, flush)

    # hide fsm_locations by default from dropdowns
    # to show them, add [("show_fsm_locations": True)] to the context
    @api.model
    def name_search(self, name="", args=None, operator="ilike", limit=100):
        if not self.env.context.get("show_fsm_locations"):
            args = list(args or []) + [("fsm_location", "=", False)]
        return super().name_search(name=name, args=args, operator=operator, limit=limit)
