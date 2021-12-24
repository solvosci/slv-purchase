# © 2021 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html
{
    "name": "Purchase Order - Due Date based on Stock Pickings",
    "summary": """
        Adds a computed Due Date for a Purchase Order,
        like Invoice Does, based on last done picking date
    """,
    "author": "Solvos",
    "license": "AGPL-3",
    "version": "13.0.1.0.0",
    'category': "Operations/Purchase",
    "website": "https://github.com/solvosci/slv-purchase",
    "depends": ["account_payment_term_extension", "purchase_stock"],
    "data": [
        "views/purchase_order_views.xml"
    ],
    'installable': True,
}
