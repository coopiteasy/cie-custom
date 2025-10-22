# SPDX-FileCopyrightText: 2022 Coop IT Easy SC
#
# SPDX-License-Identifier: AGPL-3.0-or-later

from odoo import api, fields, models
from odoo.tools.safe_eval import safe_eval


class ResPartner(models.Model):
    _inherit = "res.partner"

    current_membership_line_id = fields.Many2one(
        comodel_name="membership.membership_line",
        string="Current Membership",
        compute="_compute_current_membership_line_id",
        # This is needed because other computed fields depend on this one.
        search="_search_current_membership_line_id",
    )
    expenditure_ceiling_current_period_start_date = fields.Date(
        string="Start Date of Current Expenditure Period",
        related="current_membership_line_id.expenditure_ceiling_current_period_start_date",
    )
    expenditure_ceiling_current_period_end_date = fields.Date(
        string="End Date of Current Expenditure Period",
        related="current_membership_line_id.expenditure_ceiling_current_period_end_date",
    )
    expenditure_ceiling_current = fields.Monetary(
        string="Current Expenditure Ceiling",
        related="current_membership_line_id.expenditure_ceiling_current",
    )

    expenditure_ceiling_current_total_sale_amount = fields.Monetary(
        compute="_compute_expenditure_ceiling_current_total_sale_amount"
    )
    expenditure_ceiling_current_remaining_amount = fields.Monetary(
        compute="_compute_expenditure_ceiling_current_total_sale_amount"
    )

    @api.depends(
        "expenditure_ceiling_current_period_start_date",
        "expenditure_ceiling_current_period_end_date",
        "pos_order_ids",
    )
    def _compute_expenditure_ceiling_current_total_sale_amount(self):
        for partner in self:
            if (
                partner.expenditure_ceiling_current_period_start_date
                and partner.expenditure_ceiling_current_period_end_date
            ):
                current_orders = partner.mapped("pos_order_ids").filtered(
                    lambda x: x.date_order.date()
                    >= partner.expenditure_ceiling_current_period_start_date
                    and x.date_order.date()
                    <= partner.expenditure_ceiling_current_period_end_date
                )
                partner.expenditure_ceiling_current_total_sale_amount = sum(
                    current_orders.mapped("amount_total")
                )
            else:
                partner.expenditure_ceiling_current_total_sale_amount = 0
            partner.expenditure_ceiling_current_remaining_amount = (
                partner.expenditure_ceiling_current
                - partner.expenditure_ceiling_current_total_sale_amount
            )

    @api.depends(
        "member_lines",
        "member_lines.date_from",
        "member_lines.date_to",
        "member_lines.state",
    )
    def _compute_current_membership_line_id(self):
        today = fields.date.today()
        for partner in self:
            membership_lines = partner.member_lines.filtered(
                lambda line: (not line.date_from or line.date_from <= today)
                and (not line.date_to or line.date_to >= today)
                and line.state in ("free", "paid")
            ).sorted("date_from", reverse=True)
            if membership_lines:
                partner.current_membership_line_id = membership_lines[0]
            else:
                partner.current_membership_line_id = False

    # FIXME: Maybe move this to another module.
    @api.depends(
        "current_membership_line_id",
        "member_lines.membership_id.membership_pricelist_id",
    )
    def _compute_product_pricelist(self):
        res = super()._compute_product_pricelist()
        # This overrides existing functionality, but only if a membership was
        # found.
        for partner in self:
            if partner.current_membership_line_id:
                membership = partner.current_membership_line_id
                partner.property_product_pricelist = (
                    membership.membership_id.membership_pricelist_id
                )
        return res

    def _search_current_membership_line_id(self, operator, value):
        if operator not in ("=", "!=", ">", ">=", "<", "<=", "=?", "in", "not in"):
            return []

        if operator in ["=", "=?"]:
            operator = "=="

        # Terrible hack. There exists no way to create a domain for the current
        # membership line id using only stored values, so we simply forcibly
        # compute the value and compare against the IDs.
        filter_string = (
            "partner.current_membership_line_id.id {operator} {value}".format(
                operator=operator, value=value
            )
        )
        filtered = filtered = self.search([]).filtered(
            lambda partner: safe_eval(
                filter_string,
                {"partner": partner},
            )
        )
        if filtered:
            return [("id", "in", [partner.id for partner in filtered])]
        return []
