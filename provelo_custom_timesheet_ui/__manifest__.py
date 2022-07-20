# Copyright 2022 Coop IT Easy SC
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Pro Velo Custom Timesheets UI",
    "summary": """
        Small modifications to the Timesheets UI""",
    "version": "12.0.1.0.0",
    "category": "Human Resources",
    "website": "https://coopiteasy.be",
    "author": "Coop IT Easy SC",
    "license": "AGPL-3",
    "application": False,
    "depends": [
        "hr_timesheet_overtime",
    ],
    "excludes": [],
    "data": [
        "views/hr_timesheet_sheet_views.xml",
    ],
    "demo": [],
    "qweb": [],
}
