from odoo import api, fields, models


# todo move printing functions to specific module
class RequestLabelPrintingWizard(models.TransientModel):
    _inherit = "label.printing.wizard"

    @api.multi
    def request_printing(self):
        self.ensure_one()
        if not self.env.user.has_group(
            "beesdoo_product_info_screen.group_product_info_user"
        ):
            super().request_printing()
        else:
            self.product_ids.sudo().write({"label_to_be_printed": True})

    @api.multi
    def set_as_printed(self):
        self.ensure_one()
        if not self.env.user.has_group(
            "beesdoo_product_info_screen.group_product_info_user"
        ):
            super().set_as_printed()
        else:
            self.product_ids.sudo().write(
                {
                    "label_to_be_printed": False,
                    "label_last_printed": fields.Datetime.now(),
                }
            )
