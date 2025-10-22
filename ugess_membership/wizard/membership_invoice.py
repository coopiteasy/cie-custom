# SPDX-FileCopyrightText: 2022 Coop IT Easy SC
#
# SPDX-License-Identifier: AGPL-3.0-or-later

from odoo import api, fields, models

from ..models.membership_membership_line import (
    EXPENDITURE_CEILING_HELP,
    EXPENDITURE_CEILING_PERIOD_HELP,
)


class MembershipInvoice(models.TransientModel):
    _inherit = "membership.invoice"

    social_project_id = fields.Many2one(
        comodel_name="social.project",
        string="Social Project",
        domain="[('partner_id', '=', partner_id)]",
        required=False,
    )
    comment = fields.Text(string="Comment")

    company_id = fields.Many2one(
        comodel_name="res.company",
        required=True,
        readonly=True,
        default=lambda self: self.env.company,
    )
    currency_id = fields.Many2one(
        comodel_name="res.currency",
        related="company_id.currency_id",
        readonly=True,
    )
    expenditure_ceiling = fields.Monetary(
        string="Expenditure Ceiling",
        help=EXPENDITURE_CEILING_HELP,
    )
    expenditure_ceiling_period = fields.Selection(
        selection=[
            ("week", "Week"),
            ("month", "Month"),
            ("year", "Year"),
        ],
        string="Expenditure Ceiling Period",
        help=EXPENDITURE_CEILING_PERIOD_HELP,
        default="month",
        required=True,
    )
    expenditure_override_ids = fields.One2many(
        comodel_name="membership.invoice.override",
        inverse_name="membership_line_id",
        string="Expenditure Overrides",
    )

    partner_id = fields.Many2one(
        comodel_name="res.partner",
        string="Partner",
    )

    # usefull to be able to show the user what are
    # the dates of the membership without any side effect
    # if using date_from and date_to
    current_membership_date_from = fields.Date(
        string="Start Date",
        readonly=True,
    )
    current_membership_date_to = fields.Date(
        string="End Date",
        readonly=True,
    )

    @api.onchange("social_project_id")
    def _onchange_social_project_id(self):
        self.date_from = self.social_project_id.start_date
        self.date_to = self.social_project_id.end_date

    def _get_current_membership_dates(self, product_id):
        """for the variable type i rely on the computation
        made on the account.move.line"""

        if product_id.membership_type == "variable":
            params = self.env["account.move.line"]._prepare_membership_line(
                self.env["account.move"].browse(),
                product_id,
                None,
                None,
            )
            date_from = params["date_from"]
            date_to = params["date_to"]
        elif product_id.membership_type == "custom":
            # TODO: Ought this not be `date_X = self.date_X`?
            date_from = False
            date_to = False
        else:
            date_from = product_id.membership_date_from
            date_to = product_id.membership_date_to

        self.current_membership_date_from = date_from
        self.current_membership_date_to = date_to

        return (date_from, date_to)

    @api.onchange("product_id")
    def onchange_product(self):
        (self.date_from, self.date_to) = self._get_current_membership_dates(
            self.product_id
        )

    def membership_invoice(self):
        res = super().membership_invoice()

        account_moves = self.env["account.move"].search(res["domain"])
        membership_lines = account_moves.mapped("invoice_line_ids.membership_lines")
        membership_lines.write(
            {
                "social_project_id": self.social_project_id,
                "comment": self.comment,
                "expenditure_ceiling": self.expenditure_ceiling,
                "expenditure_ceiling_period": self.expenditure_ceiling_period,
                "expenditure_override_ids": [
                    (
                        fields.Command.CREATE,
                        None,
                        {
                            "date_from": override.date_from,
                            "date_to": override.date_to,
                            "expenditure_ceiling": override.expenditure_ceiling,
                        },
                    )
                    for override in self.expenditure_override_ids
                ],
            }
        )

        return res
