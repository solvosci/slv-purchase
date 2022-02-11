# © 2022 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html
{
    "name": "Purchase Order - Batch Confirm & Receive products",
    "summary": """
        Adds an action that makes confirmation and reception
        for purchase orders in one click
    """,
    "author": "Solvos",
    "license": "LGPL-3",
    "version": "13.0.1.1.0",
    'category': "Operations/Purchase",
    "website": "https://github.com/solvosci/slv-purchase",
    "depends": ["purchase_stock"],
    "data": [
        "views/purchase_order_views.xml"
    ],
    'installable': True,
}
