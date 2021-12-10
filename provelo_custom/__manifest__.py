# Copyright 2021 Coop IT Easy SCRL fs
#   Robin Keunen <robin@coopiteasy.be>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    "name": "Provelo Customizations",
    "version": "12.0.1.0.0",
    "depends": [
        "account",
        "sale",
        "resource_activity",
        "hr_holidays",
        "hr_timesheet_sheet",
        "hr_timesheet_activity_begin_end",
        "l10n_be_invoice_bba",
        "csv_export_partner",
        "csv_export_invoice",
        "csv_export_payment",
    ],
    "author": "Coop IT Easy SCRLfs",
    "license": "AGPL-3",
    "category": "",
    "website": "https://coopiteasy.be",
    "summary": "Pro Vélo customizations",
    "data": [
        "views/account_payment_view.xml",
        "views/hr_holidays_view.xml",
        "views/hr_leave_report_views.xml",
        "views/hr_leave_views.xml",
        "views/hr_timesheet_sheet_view.xml",
        "views/location_filters.xml",
        "views/res_partner_views.xml",
        "report/hr_leave_report.xml",
        "report/layout.xml",
        "views/hr_kanban_views_employees.xml",
        # "report/available_holidays_view.xml", fixme
        "report/report_invoice.xml",
        "security/security.xml",
        "security/ir.model.access.csv",
        "wizard/hr_holidays_summary_department_view.xml",
        "data/data.xml",
        "data/sftp.xml",
    ],
    "installable": True,
}
