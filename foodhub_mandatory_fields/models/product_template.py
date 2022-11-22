from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    volume = fields.Float(required="True")
    weight = fields.Float(required="True")
    seller_ids = fields.One2many(required="True")
    description_sale = fields.Text(required="True")
    public_categ_ids = fields.Many2many(required="True")
    pos_categ_id = fields.Many2one(required="True")
    list_price = fields.Float(required="True")
    hs_code_id = fields.Many2one(required="True")
    default_code = fields.Char(required="True")
