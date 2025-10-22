# Copyright 2022 Akretion (https://www.akretion.com).
# @author Pierrick Brun <pierrick.brun@akretion.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class SupplySource(models.Model):
    _name = "supply.source"
    _description = "The source of the supply (financially or materially)"

    name = fields.Char(required=True)
