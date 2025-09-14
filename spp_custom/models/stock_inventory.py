# Copyright 2020 Coop IT Easy SCRL fs
#   Manuel Claeys Bouuaert <manuel@coopiteasy.be>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class InventoryAdjustmentsGroup(models.Model):
    _inherit = "stock.inventory"

    product_selection = fields.Selection(default="manual")
