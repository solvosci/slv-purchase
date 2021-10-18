# © 2021 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html
{
    "name": "Purchase Order Type Advanced",
    "summary": """
        Adds extra fields to the purchase order type (journal, picking type,...)
    """,
    "author": "Solvos",
    "license": "LGPL-3",
    "version": "13.0.1.0.2",
    'category': "Operations/Purchase",
    "website": "https://github.com/solvosci/slv-purchase",
    "depends": [
        "purchase_stock",
        "purchase_order_type"
    ],
    "data": [
        "views/purchase_order_type_views.xml",
        "views/account_move_views.xml"
    ],
    'installable': True,
}
