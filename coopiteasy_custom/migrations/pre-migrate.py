# Copyright 2021 ForgeFlow S.L. (https://www.forgeflow.com)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openupgradelib import openupgrade

# xmlid_renames = [
#     (
#         "coopiteasy_custom.helpesk_ticket_personal_rule",
#         "helpdesk_mgmt.helpdesk_ticket_personal_rule",
#     ),
# ]


@openupgrade.migrate()
def migrate(env, version):
    # openupgrade.rename_xmlids(env.cr, xmlid_renames)
    for task in env["project.task"].search([]):
        if task.link_task_ids:
            task.project_id.allow_task_dependencies = True
            task.write({"depend_on_ids": task.link_task_ids})
    env.cr.commit()
