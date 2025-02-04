{
    "name": "Foodhub Picking Operations",
    "version": "16.0.1.0.0",
    "summary": """
        Foodhub customizations : sort picking operations by category and reference""",
    "author": "Coop IT Easy SC",
    "website": "https://coopiteasy.be",
    "license": "AGPL-3",
    "category": "Stock",
    "depends": ["stock", "sale_management"],
    "data": [
        "reports/report_picking.xml",
        "views/stock_picking_views.xml",
        "views/sale_order_line_views.xml",
    ],
}
