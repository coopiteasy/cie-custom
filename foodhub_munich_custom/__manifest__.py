# Copyright 2021 Coop IT Easy SCRLfs
# 	    Vincent Van Rossem <vincent@coopiteasy.be>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Foodhub Munich Custom",
    "version": "12.0.1.0.0",
    "summary": """
        Foodhub Munich customizations""",
    "author": "Coop IT Easy SCRL fs",
    "website": "https://coopiteasy.be",
    "license": "AGPL-3",
    "category": "Cooperative management",
    "depends": ["easy_my_coop"],
    "data": [
        "report/easy_my_coop_report.xml",
        "report/cooperator_membership_declaration.xml",
        "data/mail_template_data.xml",  # must be loaded after reports
    ],
}
