from werkzeug.exceptions import NotFound

from odoo import http
from odoo.exceptions import AccessError
from odoo.http import request

from odoo.addons.mail.controllers.discuss import DiscussController


class UGESSDiscussController(DiscussController):
    @http.route()
    def mail_init_messaging(self, **kwargs):
        try:
            return super().mail_init_messaging(**kwargs)
        except AccessError:
            if request.env.user.has_group("base.group_user"):
                return request.env.user.sudo()._init_messaging()
        raise NotFound()
