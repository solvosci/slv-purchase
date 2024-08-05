# © 2024 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html
{
    "name": "Sale Purchase Customer",
    "summary": """
        Add field to fill with the customer associated to a purchase.
    """,
    "author": "Solvos",
    "license": "LGPL-3",
    "version": "14.0.1.0.0",
    'category': "Operations/Purchase",
    "website": "https://github.com/solvosci/slv-purchase",
    "depends": [
        "sale_purchase",
    ],
    "data": [
        "views/purchase_order.xml",
    ],
    'installable': True,
    "pre_init_hook": "pre_init_hook",
}
