# SPDX-FileCopyrightText: 2022 Coop IT Easy SC
#
# SPDX-License-Identifier: AGPL-3.0-or-later

{
    "name": "RotorDC Mail Activity Display Info",
    "summary": """
        Display the info of activities by default.""",
    "version": "12.0.1.0.0",
    "category": "Discuss",
    "website": "https://coopiteasy.be",
    "author": "Coop IT Easy SC",
    "maintainers": ["carmenbianca"],
    "license": "AGPL-3",
    "application": False,
    "depends": [
        "mail",
    ],
    "excludes": [],
    "data": [
        "data/mail_data.xml",
    ],
    "demo": [],
    "qweb": [
        "static/src/xml/activity.xml",
    ],
}
