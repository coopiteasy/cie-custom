# Copyright 2021 Coop IT Easy SCRL fs
#   Robin Keunen <robin@coopiteasy.be>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
{
    "name": "Pro Velo Resource Activity Reports",
    "version": "12.0.1.0.0",
    "depends": [
        "resource_activity_delivery",
        "resource_activity_guide",
        "provelo_analytic_account",
    ],
    "author": "Coop IT Easy SC",
    "category": "Resource",
    "website": "https://coopiteasy.be",
    "license": "AGPL-3",
    "summary": """
        Reports for resource activities
    """,
    "data": [
        "security/ir.model.access.csv",
        "reports/resource_activity_report_view.xml",
        "reports/resource_activity_registration_report_view.xml",
    ],
    "installable": True,
}
