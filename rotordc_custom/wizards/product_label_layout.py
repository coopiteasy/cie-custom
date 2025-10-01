# SPDX-FileCopyrightText: 2024 Coop IT Easy SC
#
# SPDX-License-Identifier: AGPL-3.0-or-later

from odoo import fields, models


class ProductLabelLayout(models.TransientModel):
    _inherit = "product.label.layout"

    print_format = fields.Selection(
        selection_add=[("dymo_rotordc", "Dymo (RotorDC)"), ("2x7xprice",)],
        ondelete={"dymo_rotordc": "set default"},
        default="dymo_rotordc",
    )

    def _prepare_report_data(self):
        xml_id, data = super()._prepare_report_data()
        if self.print_format == "dymo_rotordc":
            xml_id = "rotordc_custom.report_product_template_label_dymo_rotordc"
        return xml_id, data
