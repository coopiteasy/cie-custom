# SPDX-FileCopyrightText: 2024 Coop IT Easy SC
#
# SPDX-License-Identifier: AGPL-3.0-or-later

from odoo import fields, models


class ResourceResource(models.Model):
    _inherit = "resource.resource"

    pv_project_id = fields.Many2one(
        "pv.project",
        string="Pro Velo Project",
    )
