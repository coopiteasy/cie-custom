# Copyright 2024 Coop IT Easy SC
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openupgradelib import openupgrade

# field definition in v12 of coopiteasy_custom
#     link_task_ids = fields.Many2many(
#         comodel_name="project.task",
#         relation="link_task_relation_table",
#         column1="user1_id",
#         column2="user2_id",
#         string="Linked Tasks",

# field definition in v16 of project
#     depend_on_ids = fields.Many2many(
#         "project.task",
#         relation="task_dependencies_rel",
#         column1="task_id",
#         column2="depends_on_id",
#         string="Blocked By",
#         tracking=True,
#         copy=False,
#         domain="[('project_id', '!=', False), ('id', '!=', id)]",
#     )


@openupgrade.migrate()
def migrate(env, version):
    # there are no hierarchy in linked task field,
    # I assume col 1 (user1_id) (from here the linked task
    # are added) is the blocked task
    env.cr.execute(
        """
    insert into task_dependencies_rel
        select user1_id, user2_id from link_task_relation_table;
    """
    )
    env.cr.commit()
