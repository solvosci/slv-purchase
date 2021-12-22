# © 2021 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html
{
    "name": "Purchase Order Batch Import - Onchnage methods",
    "summary": """
        Adds an action that finishes an Odoo purchase order importation
    """,
    "author": "Solvos",
    "license": "LGPL-3",
    "version": "13.0.1.0.0",
    'category': "Operations/Purchase",
    "website": "https://github.com/solvosci/slv-purchase",
    "depends": [
        "purchase_order_partner_user",
        "purchase_order_type",
    ],
    "data": [
        "views/purchase_order_views.xml"
    ],
    'installable': True,
}
