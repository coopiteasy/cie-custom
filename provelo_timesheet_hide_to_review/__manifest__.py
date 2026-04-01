# SPDX-FileCopyrightText: 2022 Coop IT Easy SC
#
# SPDX-License-Identifier: AGPL-3.0-or-later

{
    "name": "Pro Velo Timesheet Hide To Review",
    "summary": """
        Hide 'To Review' menu from the top bar.""",
    "version": "12.0.1.0.0",
    "category": "Human Resources",
    "website": "https://coopiteasy.be",
    "author": "Coop IT Easy SC",
    "maintainers": ["carmenbianca"],
    "license": "AGPL-3",
    "application": False,
    "depends": [
        "hr_timesheet_sheet",
    ],
    "excludes": [],
    "data": [
        "views/hr_timesheet_sheet_views.xml",
    ],
    "demo": [],
    "qweb": [],
}
