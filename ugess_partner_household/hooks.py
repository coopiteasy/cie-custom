# SPDX-FileCopyrightText: 2022 Coop IT Easy SC
#
# SPDX-License-Identifier: AGPL-3.0-or-later

import logging

from odoo import SUPERUSER_ID, api

_logger = logging.getLogger(__name__)


def post_init_hook(cr, registry):
    _logger.info("Creating linked members for all partners")
    env = api.Environment(cr, SUPERUSER_ID, {})
    env["res.partner"].search([])._create_linked_member()
    _logger.info("Done!")
