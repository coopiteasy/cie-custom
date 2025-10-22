from openupgradelib import openupgrade


@openupgrade.migrate()
def migrate(env, version):
    if not version:
        return

    # delete the maybe existing ir rule in membership which was faulty
    # and which we define in that module now because the company_id is
    # defined here on membership.invoice
    ir_rule = env.ref(
        "membership.rule_membership_invoice_multi_company", raise_if_not_found=False
    )
    ir_rule and ir_rule.unlink()
