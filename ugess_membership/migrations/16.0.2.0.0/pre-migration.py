# SPDX-FileCopyrightText: 2023 Coop IT Easy SC
#
# SPDX-License-Identifier: AGPL-3.0-or-later

from openupgradelib import openupgrade


@openupgrade.migrate()
def migrate(env, version):
    cr = env.cr

    if not openupgrade.column_exists(
        cr, "membership_membership_line", "expenditure_ceiling_first_period"
    ) or not openupgrade.column_exists(
        cr, "membership_membership_line", "expenditure_ceiling_first_period_end_date"
    ):
        return

    # The write/create uids are incorrect per se---the records are being created
    # by the admin user---but doing it this way is less error-prone than trying
    # to get the data right.
    openupgrade.logged_query(
        cr,
        """
        INSERT INTO membership_membership_line_expenditure_override
            (membership_line_id, date_from, date_to, expenditure_ceiling,
             create_date, create_uid, write_date, write_uid)
        SELECT
            mml.id AS membership_line_id,
            mml.date_from AS date_from,
            mml.expenditure_ceiling_first_period_end_date AS date_to,
            mml.expenditure_ceiling_first_period AS expenditure_ceiling,
            CURRENT_TIMESTAMP as create_date,
            mml.create_uid as create_uid,
            CURRENT_TIMESTAMP as write_date,
            mml.write_uid as write_uid
        FROM
            membership_membership_line mml
        WHERE
            mml.expenditure_ceiling_first_period IS NOT NULL
            AND mml.expenditure_ceiling_first_period_end_date IS NOT NULL;
        """,
    )
