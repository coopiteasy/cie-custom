# SPDX-FileCopyrightText: 2022 Coop IT Easy SC
#
# SPDX-License-Identifier: AGPL-3.0-or-later

{
    "name": "UGESS Membership",
    "summary": """
        Membership subscriptions to social projects.""",
    "version": "16.0.3.0.0",
    "category": "Membership",
    "website": "https://coopiteasy.be",
    "author": "Coop IT Easy SC",
    "license": "AGPL-3",
    "application": False,
    "depends": [
        # Odoo
        "membership",
        "point_of_sale",
        # OCA
        "membership_extension",
        "partner_contact_personal_information_page",
        # Ugess
        "membership_custom_date",
        "ugess_partner_social_project",
    ],
    "excludes": [],
    "data": [
        "security/ir.model.access.csv",
        "security/membership_security.xml",
        "views/product_template_views.xml",
        "views/res_partner_views.xml",
        "views/membership_category_view.xml",
        "wizard/membership_invoice_views.xml",
    ],
    "demo": [
        "demo/membership_category.xml",
        "demo/res_partner.xml",
        "demo/product_product.xml",
    ],
    "qweb": [],
}
