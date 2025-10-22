# Copyright 2023 Akretion (http://www.akretion.com).
# @author Olivier Nibart <olivier.nibart@akretion.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import SUPERUSER_ID, Command, api


def post_init_hook(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})

    # at install add our special group to all internal users
    # to be iso functional
    env["res.users"].browse(env.ref("base.group_user").users.ids).groups_id = [
        Command.link(
            env.ref("ugess_security_user_stats.group_user_all_non_private_contacts").id
        ),
    ]


def uninstall_hook(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})

    # set back the base partner rules like they are
    # in standard odoo
    env.ref("base.res_partner_rule_private_employee").groups = [
        Command.link(env.ref("base.group_user").id)
    ]
    env.ref("base.res_partner_portal_public_rule").groups = [
        Command.unlink(env.ref("base.group_user").id),
    ]

    env.ref("hr.access_hr_employee_public_user").group_id = env.ref(
        "base.group_user"
    ).id
    env.ref("utm.access_utm_campaign_user").group_id = env.ref("base.group_user").id
