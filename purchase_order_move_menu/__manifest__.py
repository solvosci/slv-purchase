# © 2022 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html
{
    "name": "Purchase Order Move Menu",
    "summary": """
        Adds new menu for purchase related moves
    """,
    "author": "Solvos",
    "license": "LGPL-3",
    "version": "13.0.2.0.0",
    "category": "Operations/Purchase",
    "website": "https://github.com/solvosci/slv-purchase",
    "depends": ["purchase_stock"],
    "data": [
        "views/stock_move_views.xml",
        "views/purchase_order_views.xml",
    ],
    'installable': True,
}
