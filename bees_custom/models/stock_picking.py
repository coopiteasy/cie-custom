# Copyright 2021 Coop IT Easy SCRL fs
#   Carmen Bianca Bakker <carmen@coopiteasy.be>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class Picking(models.Model):
    _inherit = "stock.picking"

    zero_received_move_ids = fields.One2many(
        "stock.move",
        string="Stock moves that were not received",
        compute="_compute_zero_received",
    )
    too_few_received_move_ids = fields.One2many(
        "stock.move",
        string="Stock moves of which too few were received",
        compute="_compute_too_few_received",
    )
    too_many_received_move_ids = fields.One2many(
        "stock.move",
        string="Stock moves of which too many were received",
        compute="_compute_too_many_received",
    )

    @api.depends("move_lines")
    def _compute_zero_received(self):
        for pick in self:
            pick.zero_received_move_ids = pick._filtered_moves().filtered(
                lambda move: move.quantity_done == 0 and move.product_qty
            )

    @api.depends("move_lines")
    def _compute_too_few_received(self):
        for pick in self:
            pick.too_few_received_move_ids = pick._filtered_moves().filtered(
                lambda move: move.quantity_done < move.product_qty
            )

    @api.depends("move_lines")
    def _compute_too_many_received(self):
        for pick in self:
            pick.too_many_received_move_ids = pick._filtered_moves().filtered(
                lambda move: move.quantity_done > move.product_qty
            )

    @api.multi
    def action_done(self):
        self._notify_incorrect_delivery()

        return super(Picking, self).action_done()

    @api.multi
    def _notify_incorrect_delivery(self):
        """Send a notification e-mail about the incorrect delivery."""
        for pick in self:
            if not any(
                (
                    pick.zero_received_move_ids,
                    pick.too_few_received_move_ids,
                    pick.too_many_received_move_ids,
                )
            ):
                # TODO: Handle this case.
                continue

            self.env.ref("bees_custom.mail_template_incorrect_delivery").send_mail(
                pick.id
            )

        return True

    @api.multi
    def _filtered_moves(self):
        return self.mapped("move_lines").filtered(
            lambda move: move.state
            in ["draft", "waiting", "partially_available", "assigned", "confirmed"]
        )
