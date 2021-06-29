from odoo import models


class SubscriptionRequest(models.Model):
    _inherit = "subscription.request"

    def create_invoice(self, partner):
        invoice = super().create_invoice(partner)
        self.send_membership_declaration()
        return invoice

    def send_membership_declaration(self):
        if self.company_id.send_capital_release_email:
            mail_template = self.get_membership_declaration_mail_template()
            mail_template.sudo().send_mail(self.id, True)

    def get_membership_declaration_mail_template(self):
        template = (
            "foodhub_munich_custom.email_template_membership_declaration"
        )
        return self.env.ref(template, False)
