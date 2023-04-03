# SPDX-FileCopyrightText: 2023 Coop IT Easy SC
#
# SPDX-License-Identifier: AGPL-3.0-or-later

{
    "name": "BAO Supplier Certificate",
    "summary": """
        Custom certificates for supplier of Boucher À Oreilles""",
    "version": "16.0.1.0.0",
    "category": "Uncategorized",
    "website": "https://coopiteasy.be",
    "author": "Coop IT Easy SC",
    "maintainers": ["remytms"],
    "license": "AGPL-3",
    "application": False,
    "depends": ["purchase"],
    "excludes": [],
    "data": [
        "security/ir.model.access.csv",
        "views/supplier_certificate_generator_views.xml",
        "report/report_supplier_certificate.xml",
        "report/ir_action_report.xml",
        "data/mail_template.xml",
    ],
    "demo": [],
    "qweb": [],
}
