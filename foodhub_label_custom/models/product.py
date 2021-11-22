from odoo import fields, models


class Product(models.Model):
    _inherit = "product.template"
    producer = fields.Char(string="Producer")
    location = fields.Char(string="Location")
    distance = fields.Float(string="Distance (in km)")
