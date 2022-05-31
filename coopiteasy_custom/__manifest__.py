# Copyright 2019 Coop IT Easy SCRL fs
#   Robin Keunen <robin@coopiteasy.be>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).


{
    "name": "Coop IT Easy Customization",
    "version": "12.0.1.0.0",
    "author": "Coop IT Easy SCRLfs",
    "license": "AGPL-3",
    "category": "",
    "website": "https://coopiteasy.be",
    "summary": """
        Specific customizations for Coop IT Easy
    """,
    "depends": [
        "hr_timesheet",
        "project_status",
    ],
    "data": [
        "data/cron.xml",
        "views/account_analytic_line.xml",
        "views/project_view.xml",
    ],
    "installable": True,
}
