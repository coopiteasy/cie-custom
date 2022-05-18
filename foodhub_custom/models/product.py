from odoo import fields, models


class Product(models.Model):
    _inherit = "product.template"
    description_sale = fields.Text(translate=False)
