from odoo import http

from odoo.addons.website_sale.controllers.main import WebsiteSale


class WebsiteSale(WebsiteSale):
    @http.route(
        [
            """/shop""",
            """/shop/page/<int:page>""",
            """/shop/category/<model("product.public.category", "[('website_id', 'in', (False, current_website_id))]"):category>""",  # noqa: B950 (line too long)
            """/shop/category/<model("product.public.category", "[('website_id', 'in', (False, current_website_id))]"):category>/page/<int:page>""",  # noqa: B950 (line too long)
        ],
        type="http",
        auth="user",
        website=True,
    )
    def shop(self, page=0, category=None, search="", ppg=False, **post):
        """Change `auth` value from `public` to `user`"""
        return super().shop(
            page=page, category=category, search=search, ppg=ppg, **post
        )
