# © 2021 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html
{
    "name": "Purchase Security - Advanced",
    "summary": """
        Adds extra security for Purchase Order security schema
    """,
    "author": "Solvos",
    "license": "LGPL-3",
    "version": "13.0.1.0.0",
    'category': "Operations/Purchase",
    "website": "https://github.com/solvosci/slv-purchase",
    "depends": [
        "purchase_security",
    ],
    "data": [
        "views/purchase_order_views.xml"
    ],
    'installable': True,
}
