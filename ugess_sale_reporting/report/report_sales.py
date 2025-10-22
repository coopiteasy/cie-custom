# Copyright 2023 Akretion (https://www.akretion.com).
# @author Pierrick Brun <pierrick.brun@akretion.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models

from odoo.addons.membership.report.report_membership import STATE


class SaleReport(models.Model):
    _inherit = "sale.report"

    supplier_id = fields.Many2one("res.partner", readonly=True)
    supply_source_id = fields.Many2one("supply.source", readonly=True)
    weight = fields.Float(digits="Stock Weight", readonly=True)
    ugess_average_market_price = fields.Float(readonly=True)
    ugess_savings_compared_to_market = fields.Float(readonly=True)
    current_membership_state = fields.Selection(STATE, readonly=True)
    total_cost = fields.Float(readonly=True)
    membership_category_id = fields.Many2one(
        "membership.membership_category", readonly=True
    )
    membership_id = fields.Many2one("product.product", readonly=True)
    categ_level_1_id = fields.Many2one("product.category", readonly=True)
    categ_level_2_id = fields.Many2one("product.category", readonly=True)
    categ_level_3_id = fields.Many2one("product.category", readonly=True)

    nbr_orders = fields.Integer(group_operator="count_distinct", readonly=True)
    nbr_households = fields.Integer(group_operator="count_distinct", readonly=True)
    avg_persons_in_household = fields.Float(group_operator="avg", readonly=True)

    # Qties can be weights so we want the third digit
    product_uom_qty = fields.Float(digits="Stock Weight", readonly=True)
    qty_to_deliver = fields.Float(digits="Stock Weight", readonly=True)
    qty_delivered = fields.Float(digits="Stock Weight", readonly=True)
    qty_to_invoice = fields.Float(digits="Stock Weight", readonly=True)
    qty_invoiced = fields.Float(digits="Stock Weight", readonly=True)

    def _select_additional_fields(self):
        res = super()._select_additional_fields()
        # MAX is used to avoid having to group by this field
        # There is no harm in using it since we are already grouped by template
        res["supply_source_id"] = "MAX(t.supply_source_id)"
        res["supplier_id"] = "MAX(t.supplier_id)"
        res[
            "ugess_average_market_price"
        ] = "SUM(product_uom_qty * t.ugess_average_market_price)"
        # price_total formula in sale
        res[
            "ugess_savings_compared_to_market"
        ] = f"""
            SUM(product_uom_qty * t.ugess_average_market_price)
            - (SUM(l.price_total)
                * {self._case_value_or_one('s.currency_rate')}
                * {self._case_value_or_one('currency_table.rate')}
            )"""
        res["current_membership_state"] = "partner.membership_state"
        res["total_cost"] = "SUM(l.purchase_price * l.product_uom_qty)"
        res["membership_id"] = "membership.id"
        res["membership_category_id"] = "membership_tmpl.membership_category_id"
        res["nbr_orders"] = "order_id"
        res["nbr_households"] = "partner_id"
        res["avg_persons_in_household"] = "AVG(partner.number_of_persons_in_household)"
        res["categ_level_3_id"] = "categ_level_3.id"
        res["categ_level_2_id"] = "categ_level_2.id"
        res["categ_level_1_id"] = "categ_level_1.id"
        return res

    # For compatibility with pos_sale (else all these fields are None for pos_orders)
    def _fill_pos_fields(self, additional_fields):
        res = super()._fill_pos_fields(additional_fields)
        res["supply_source_id"] = "MAX(t.supply_source_id)"
        res["supplier_id"] = "MAX(t.supplier_id)"
        res["ugess_average_market_price"] = "SUM(l.total_without_any_discount)"
        res[
            "ugess_savings_compared_to_market"
        ] = """
            SUM(l.total_without_any_discount)
            - SUM(l.price_subtotal_incl)
            """
        res["current_membership_state"] = "partner.membership_state"
        res["total_cost"] = "SUM(l.total_cost)"
        res["membership_id"] = "membership.id"
        res["membership_category_id"] = "membership_tmpl.membership_category_id"
        res["nbr_orders"] = "order_id"
        res["nbr_households"] = "partner_id"
        res["avg_persons_in_household"] = "AVG(partner.number_of_persons_in_household)"
        res["categ_level_3_id"] = "categ_level_3.id"
        res["categ_level_2_id"] = "categ_level_2.id"
        res["categ_level_1_id"] = "categ_level_1.id"
        return res

    def _group_by_sale(self):
        res = super()._group_by_sale()
        res += """,
            partner.membership_state
            , membership.id
            , membership_tmpl.membership_category_id
            , categ_level_3.id
            , categ_level_2.id
            , categ_level_1.id
            """
        return res

    def _group_by_pos(self):
        res = super()._group_by_pos()
        res += """
            , partner.membership_state
            , membership.id
            , membership_tmpl.membership_category_id
            , categ_level_3.id
            , categ_level_2.id
            , categ_level_1.id
            """
        return res

    def _from_sale(self):
        res = super()._from_sale()
        res += """
        LEFT JOIN membership_membership_line ml ON ml.id = s.current_membership_line_id
        LEFT JOIN product_product membership ON membership.id = ml.membership_id
        LEFT JOIN product_template membership_tmpl
            ON membership_tmpl.id = membership.product_tmpl_id
        LEFT JOIN product_category categ_level_3
            ON t.categ_id = categ_level_3.id AND categ_level_3.level = 3
        LEFT JOIN product_category categ_level_2
            ON (t.categ_id = categ_level_2.id AND categ_level_2.level = 2)
            OR (categ_level_3.parent_id = categ_level_2.id AND categ_level_2.level = 2)
        LEFT JOIN product_category categ_level_1
            ON (t.categ_id = categ_level_1.id AND categ_level_1.level = 1)
            OR (categ_level_2.parent_id = categ_level_1.id AND categ_level_1.level = 1)
        """
        return res

    def _from_pos(self):
        res = super()._from_pos()
        res += """
        LEFT JOIN membership_membership_line ml ON ml.id = pos.current_membership_line_id
        LEFT JOIN product_product membership ON membership.id = ml.membership_id
        LEFT JOIN product_template membership_tmpl
            ON membership_tmpl.id = membership.product_tmpl_id
        LEFT JOIN product_category categ_level_3
            ON t.categ_id = categ_level_3.id AND categ_level_3.level = 3
        LEFT JOIN product_category categ_level_2
            ON (t.categ_id = categ_level_2.id AND categ_level_2.level = 2)
            OR (categ_level_3.parent_id = categ_level_2.id AND categ_level_2.level = 2)
        LEFT JOIN product_category categ_level_1
            ON (t.categ_id = categ_level_1.id AND categ_level_1.level = 1)
            OR (categ_level_2.parent_id = categ_level_1.id AND categ_level_1.level = 1)
        """
        return res
