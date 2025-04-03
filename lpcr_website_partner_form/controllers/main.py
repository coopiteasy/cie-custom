# SPDX-FileCopyrightText: 2025 Coop IT Easy SC
#
# SPDX-License-Identifier: AGPL-3.0-or-later

import json

from odoo import _
from odoo.http import request

from odoo.addons.website.controllers.form import WebsiteForm


class WebsitePartnerForm(WebsiteForm):
    def _handle_website_form(self, model_name, **kwargs):
        if kwargs.get("form_type") == "customer_form":
            email = kwargs.get("email")
            company_id = kwargs.get("company_id")
            if email is not None:
                domain = [("email", "=", email)]
                if company_id is not None and company_id.isdigit():
                    domain += [("company_id", "=", int(company_id))]
                existing_partner = (
                    request.env["res.partner"]
                    .sudo()
                    .search_read(
                        domain,
                        ["id", "email", "company_id"],
                        limit=1,
                    )
                )
                if existing_partner:
                    return json.dumps({"error": _("E-mail address already used.")})
        return super()._handle_website_form(model_name=model_name, **kwargs)
