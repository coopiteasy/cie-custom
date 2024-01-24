# Copyright 2024 Coop IT Easy SC
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openupgradelib import openupgrade


@openupgrade.migrate()
def migrate(env, version):
    env.cr.execute(
        """
    alter table project_task drop column if exists reviewer_id;
    alter table project_task drop column if exists tester_id;
    alter table project_task drop column if exists int_priority;
    drop table link_task_relation_table;
    """
    )
    env.cr.commit()
