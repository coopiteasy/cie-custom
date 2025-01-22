from odoo import fields, models


class ResCompany(models.Model):
    _inherit = "res.company"

    nb_subscribers = fields.Integer(compute="_compute_company_data")
    nb_cooperators = fields.Integer(compute="_compute_company_data")

    def _compute_company_data(self):
        for company in self:
            company.nb_subscribers = (
                self.env["res.partner"].sudo().search_count([("subscriber", "=", True)])
            )
            company.nb_cooperators = (
                self.env["cooperative.membership"]
                .sudo()
                .search_count([("company_id", "=", company.id), ("member", "=", True)])
            )
