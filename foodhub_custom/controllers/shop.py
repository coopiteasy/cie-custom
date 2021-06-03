from odoo.addons.website_sale.controllers.main import WebsiteSale
from odoo import http


class WebsiteSale(WebsiteSale):
    @http.route([
        '''/shop''',
        '''/shop/page/<int:page>''',
        '''/shop/category/<model("product.public.category", "[('website_id', 'in', (False, current_website_id))]"):category>''',
        '''/shop/category/<model("product.public.category", "[('website_id', 'in', (False, current_website_id))]"):category>/page/<int:page>'''
    ], type='http', auth="user", website=True)
    def shop(self, page=0, category=None, search='', ppg=False, **post):
        return super(WebsiteSale, self).shop(
            page=0, category=None, search='', ppg=False, **post
        )
