# Copyright 2021 Coop IT Easy SCRL fs
#   Robin Keunen <robin@coopiteasy.be>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).


from odoo import api, fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    consignment_ids = fields.Many2many(
        comodel_name="account.tax",
        string="Consignments",
        compute="_compute_consignments",
        help="Filters taxes on product to those having 'Consigne' in their names",
    )

    @api.multi
    @api.depends("taxes_id")
    def _compute_consignments(self):
        for product in self:
            consigments = product.taxes_id.filtered(
                lambda t: "Consigne" in t.name
            )
            product.consignment_ids = consigments
