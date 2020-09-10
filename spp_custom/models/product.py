# Copyright 2020 Coop IT Easy SCRL fs
#   Robin Keunen <robin@coopiteasy.be>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

import logging

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError

_logger = logging.getLogger(__name__)


class ProductTemplate(models.Model):
    _inherit = "product.template"

    name = fields.Char(track_visibility="onchange")
    list_price = fields.Float(track_visibility="onchange")
    uom_id = fields.Many2one(track_visibility="onchange")
    uom_po_id = fields.Many2one(track_visibility="onchange")
    default_code = fields.Char(track_visibility="onchange")
    sale_ok = fields.Boolean(track_visibility="onchange")
    available_in_pos = fields.Boolean(track_visibility="onchange")

    @api.multi
    def write(self, vals):
        # Custom track visibility for
        # taxes_id (M2M), seller_ids (M2M, supplier_taxes_id (O2M)
        for rec in self:
            taxes_id_old = ""
            supplier_taxes_id_old = ""
            seller_ids_old = ""
            if "taxes_id" in vals:
                taxes_id_old = ", ".join([tax.name for tax in rec.taxes_id])
            if "supplier_taxes_id" in vals:
                supplier_taxes_id_old = ", ".join(
                    [tax.name for tax in rec.supplier_taxes_id]
                )
            if "seller_ids" in vals:
                seller_ids_old = ", ".join(
                    [
                        s.name.name + " (" + str(s.price) + ")"
                        for s in rec.seller_ids
                    ]
                )
            res = super(ProductTemplate, self).write(vals)
            if "taxes_id" in vals:
                taxes_id_new = ", ".join([tax.name for tax in rec.taxes_id])
                rec.message_post(
                    body="Customer Taxes: "
                    + taxes_id_old
                    + " → "
                    + taxes_id_new
                )
            if "supplier_taxes_id" in vals:
                supplier_taxes_id_new = ", ".join(
                    [tax.name for tax in rec.supplier_taxes_id]
                )
                rec.message_post(
                    body="Vendor Taxes: "
                    + supplier_taxes_id_old
                    + " → "
                    + supplier_taxes_id_new
                )
            if "seller_ids" in vals:
                seller_ids_new = ", ".join(
                    [
                        s.name.name + " (" + str(s.price) + ")"
                        for s in rec.seller_ids
                    ]
                )
                rec.message_post(
                    body="Vendor Pricelist: "
                    + seller_ids_old
                    + " → "
                    + seller_ids_new
                )
        return res

    @api.multi
    def generate_ref_code(self, prefix, sequence):
        for product in self:
            number = sequence.next_by_id()
            code = prefix + number

            while self.search([("default_code", "=", code)]) and number < 1000:
                number = sequence.next_by_id()
                code = prefix + number

            if number == 1000:
                _logger.error(
                    "maximum inscrementation number (1000) reached for sequence %s."
                    " It needs to be reset."
                )
                raise ValidationError(
                    _(
                        "You have reached the limit for default code generation."
                        " Please contact your system administrator.\n\n"
                        "%s" % sequence
                    )
                )

            product.default_code = code
        self.generate_barcode()

    @api.multi
    def generate_ref_code_pp(self):
        sequence = self.env.ref(
            "spp_custom.seq_ean_product_internal_ref_weight_pp"
        )
        self.generate_ref_code("01", sequence)

    @api.multi
    def generate_ref_code_bio_producer(self):
        sequence = self.env.ref(
            "spp_custom.seq_ean_product_internal_ref_weight_bio_producer"
        )
        self.generate_ref_code("02", sequence)

    @api.multi
    def generate_ref_code_bio_supplier(self):
        sequence = self.env.ref(
            "spp_custom.seq_ean_product_internal_ref_weight_bio_supplier"
        )
        self.generate_ref_code("03", sequence)

    @api.multi
    def generate_ref_code_non_bio(self):
        sequence = self.env.ref(
            "spp_custom.seq_ean_product_internal_ref_weight_non_bio"
        )
        self.generate_ref_code("09", sequence)
