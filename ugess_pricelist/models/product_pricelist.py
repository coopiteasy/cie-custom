# Copyright (C) 2023-Today GRAP (http://www.grap.coop)
# @author Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html


from odoo import fields, models


class ProductPricelist(models.Model):
    _inherit = "product.pricelist"

    ugess_type = fields.Selection(
        selection=[
            ("beneficiary", "Beneficiary"),
            ("solidary", "Solidary"),
            ("average_market", "Average Market"),
        ]
    )
