# Copyright 2019 Coop IT Easy SCRL fs
#   Robin Keunen <robin@coopiteasy.be>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).


{
    "name": "Coop IT Easy Subscriptions",
    "version": "12.0.1.0.0",
    "author": "Coop IT Easy SC",
    "license": "AGPL-3",
    "category": "Contract Management",
    "website": "https://coopiteasy.be",
    "summary": """
        Configure included support hours, compute quarter support time and invoice overshoot.
    """,
    "depends": [
        "contract",
        "project",
    ],
    "data": [
        "views/contract_views.xml",
        "views/product_template_views.xml",
    ],
    "installable": True,
}
