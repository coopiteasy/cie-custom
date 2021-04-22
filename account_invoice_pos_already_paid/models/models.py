# -*- coding: utf-8 -*-

from odoo import models, fields, api


class account(models.Model):
    _name = "account.journal"
    _inherit = "account.journal"

    used_for_pos_invoice = fields.Boolean()