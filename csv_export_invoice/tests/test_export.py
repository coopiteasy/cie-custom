# -*- coding: utf-8 -*-
# Copyright 2020 Coop IT Easy SCRL fs
#   Robin Keunen <robin@coopiteasy.be>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

import logging

from openerp.tests import common

_logger = logging.getLogger(__name__)


class TestCSVExport(common.TransactionCase):
    def test_get_rows(self):
        ICE = self.env["csv.export.invoice"]
        invoice = self.env["account.invoice"].browse(76)  # use demo data
        rows = ICE.get_rows(invoice)
        for row in rows:
            _logger.info(row)

    def test_invoice_csv_export(self):
        ice = self.env["csv.export.invoice"].create(
            {"start_date": "2019-01-01", "end_date": "2021-01-01"}
        )
        # invoice = self.env["account.invoice"].browse(1)
        ice.action_manual_export_base()