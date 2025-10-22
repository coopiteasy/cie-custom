from odoo import api, fields, models


class DataHistorizationMixin(models.AbstractModel):
    _name = "data.historization.mixin"
    _description = "Abstract model to historize data"

    historization_qty = fields.Integer(compute="_compute_historization_qty")

    _raise_historization_fields = []

    def _compute_historization_qty(self):
        for item in self:
            item.historization_qty = len(item.historization_ids)

    def _historize_items(self):
        HistorizationModel = self.env[f"data.historization.{self._name}"]
        vals_list = []
        inverse_field = self._fields.get("historization_ids").inverse_name
        for item in self.sudo():
            vals = {inverse_field: item.id}
            for field in self._historization_fields:
                if type(item._fields.get(field)) is fields.Many2one:
                    vals[field] = getattr(item, field).id
                else:
                    vals[field] = getattr(item, field)
            vals_list.append(vals)
        HistorizationModel.create(vals_list)

    @api.model_create_multi
    def create(self, vals_list):
        res = super().create(vals_list)
        res._historize_items()
        return res

    def write(self, vals):
        res = super().write(vals)
        if set(self._historization_fields + self._raise_historization_fields) & set(
            vals.keys()
        ):
            self._historize_items()
        return res
