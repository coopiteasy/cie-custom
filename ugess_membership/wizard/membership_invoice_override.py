# SPDX-FileCopyrightText: 2023 Coop IT Easy SC
#
# SPDX-License-Identifier: AGPL-3.0-or-later

from odoo import api, fields, models

from ..models.membership_membership_line_expenditure_override import ExpenditureOverride


class MembershipInvoiceOverride(models.TransientModel):
    """This is a transient version of
    membership.membership_line.expenditure.override. It's a rather annoying
    design choice. Here's the rationale:

    There's a table of overrides in the membership.invoice view (a <tree>
    element). The (transient) membership.invoice model _cannot_ have a One2many
    relationship to non-transient models. If one instead elects to use a
    Many2many relationship to the non-transient override, the UX becomes a lot
    worse, because a form view pop-up appears when clicking on 'Add a line' in
    the table, when the expected behaviour is that a new row appears. This bad
    UX persists even when writing `widget="one2many"` on the field element.

    To get around this, we create a transient version of expenditure.override.
    It has the same fields, and borrows a constraint method. Then, later, we
    simply use the values of these fields to populate the real thing.
    """

    _name = "membership.invoice.override"
    _description = "Membership Invoice Override"
    _order = "date_from asc"

    # Named as such because it's used in the copied compute function.
    membership_line_id = fields.Many2one(
        comodel_name="membership.invoice",
        string="Membership",
        required=True,
    )
    membership_line_date_from = fields.Date(
        string="Membership Start Date", related="membership_line_id.date_from"
    )
    membership_line_date_to = fields.Date(
        string="Membership End Date", related="membership_line_id.date_to"
    )
    date_from = fields.Date(string="Start Date", required=True)
    date_to = fields.Date(string="End Date", required=True)
    expenditure_ceiling_period = fields.Selection(
        related="membership_line_id.expenditure_ceiling_period",
    )
    expenditure_ceiling = fields.Monetary(
        string="New Expenditure Ceiling",
        help="New ceiling for the defined period.",
        required=True,
    )
    currency_id = fields.Many2one(
        comodel_name="res.currency",
        related="membership_line_id.currency_id",
        readonly=True,
    )

    @api.constrains(
        "date_from",
        "date_to",
    )
    def _check_valid_period(self):
        ExpenditureOverride._check_valid_period(self)
