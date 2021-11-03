##############################################################################
#
#    Copyright (C) 2017- Coop IT Easy.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
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
        "views/hr_timesheet_sheet_view.xml",
        "views/location_filters.xml",
        "views/res_partner_views.xml",
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
