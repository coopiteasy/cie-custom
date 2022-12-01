from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    # All below fields have required=True added to them.
    description_sale = fields.Text(required="True")
    public_categ_ids = fields.Many2many(required="True")
    pos_categ_id = fields.Many2one(required="True")
    list_price = fields.Float(required="True")

    # The below field have copy=True added to them.
    origin_country_id = fields.Many2one(
        copy=True,
    )

    # All below fields have both copy=True and required=True added to them.
    volume = fields.Float(required="True", copy=True)
    weight = fields.Float(required="True", copy=True)
    # FIXME: We should probably do variant_seller_ids as well. However, when
    # setting copy=True on both seller_ids and variant_seller_ids, copying
    # breaks due to a strange TypeError (NoneType object is not subscriptable).
    # Because the inverse name is identical (product_tmpl_id) for both fields,
    # it is probably _fine_ as-is.
    seller_ids = fields.One2many(
        required="True",
        copy=True,
    )
    default_code = fields.Char(required="True", copy=True)
    hs_code_id = fields.Many2one(
        required="True",
        copy=True,
    )
