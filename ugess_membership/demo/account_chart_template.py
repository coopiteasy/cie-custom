import logging
import time

from odoo import Command, api, models

_logger = logging.getLogger(__name__)


class AccountChartTemplate(models.Model):
    _inherit = "account.chart.template"

    @api.model
    def _get_demo_data_move(self):
        ref = self.env.ref
        model, data = super()._get_demo_data_move()
        data.update(
            {
                "demo_ugess_invoice_1": {
                    "move_type": "out_invoice",
                    "partner_id": ref("ugess_membership.demo_partner_beneficiary").id,
                    "invoice_user_id": ref("base.user_demo").id,
                    "invoice_payment_term_id": ref(
                        "account.account_payment_term_end_following_month"
                    ).id,
                    "invoice_date": time.strftime("%Y-%m-01"),
                    "invoice_line_ids": [
                        Command.create(
                            {
                                "product_id": ref(
                                    "ugess_membership.product_membership_beneficiary"
                                ).id,
                                "quantity": 5,
                                # Set price unit to 0 to make the invoice 'paid'
                                "price_unit": 0,
                            }
                        ),
                    ],
                },
            }
        )
        return model, data

    def _create_demo_data(self):
        res = super()._create_demo_data()
        invoice = self.env.ref("account.demo_ugess_invoice_1", False)
        partner = self.env.ref("ugess_membership.demo_partner_beneficiary", False)
        if invoice and partner:
            partner.mapped("member_lines").write(
                {
                    "expenditure_ceiling": 50,
                    "expenditure_ceiling_first_period": 30,
                    "account_invoice_line": invoice.invoice_line_ids.ids[0],
                }
            )
        return res
