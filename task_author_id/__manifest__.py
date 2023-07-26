# Copyright 2019 Coop IT Easy SCRL fs
#   Robin Keunen <robin@coopiteasy.be>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).


{
    "name": "Task Author",
    "version": "13.0.1.0.0",
    "author": "Coop IT Easy SC",
    "license": "AGPL-3",
    "category": "",
    "website": "https://coopiteasy.be",
    "summary": """
        Adds author_id field on project.task
    """,
    "depends": [
        "project",
    ],
    "data": [
        "views/project_view.xml",
    ],
    "installable": True,
}
