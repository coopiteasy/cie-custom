# Copyright 2023 Akretion (https://www.akretion.com).
# @author Pierrick Brun <pierrick.brun@akretion.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class PosOrderReport(models.Model):
    _inherit = "report.pos.order"

    supplier_id = fields.Many2one("res.partner", readonly=True)
    supply_source_id = fields.Many2one("supply.source", readonly=True)
    weight = fields.Float(digits="Stock Weight", readonly=True)

    def _select(self):
        res = super()._select()
        res += """
          , pt.supply_source_id AS supply_source_id
          , pt.supplier_id AS supplier_id
          , CASE WHEN l.product_id IS NOT NULL THEN
                SUM(p.weight * l.qty / u.factor * u.factor)
                ELSE 0 END AS weight
        """
        return res

    def _group_by(self):
        res = super(PosOrderReport, self)._group_by()
        res += """
            , pt.supplier_id
            , pt.supply_source_id
        """
        return res
