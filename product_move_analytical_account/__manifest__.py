# © 2023 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html
{
    "name": "Analytical Account to product moves",
    "summary": """
        Adds analytical account from purchase order line, to stock move line
    """,
    "author": "Solvos",
    "license": "LGPL-3",
    "version": "11.0.1.0.0",
    "category": "Inventory/Purchase",
    "website": "https://github.com/solvosci/slv-purchase",
    "depends": ["purchase"],
    "data": [
        "views/stock_move_line_views.xml",
    ],
    "post_init_hook": 'post_init_hook',
    'installable': True,
}
