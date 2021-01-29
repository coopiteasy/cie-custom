from odoo import fields, models


class PosOrderReport(models.Model):
    _inherit = "report.pos.order"

    email = fields.Char(readonly=True)
    email_formatted = fields.Char(readonly=True)

    def _select(self):
        select_str = super(PosOrderReport, self)._select()
        select_str += ", rp.email, rp.email_formatted"
        return select_str

    def _from(self):
        from_str = super(PosOrderReport, self)._from()
        from_str += " LEFT JOIN res_partner rp ON (s.partner_id=rp.id)"
        return from_str

    def _group_by(self):
        group_by_str = super(PosOrderReport, self)._group_by()
        group_by_str += ", rp.email, rp.email_formatted"
        return group_by_str
