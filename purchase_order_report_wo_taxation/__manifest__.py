# © 2021 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html
{
    "name": "Purchase Order Report Without Taxation",
    "summary": """
        Hides taxes data in purchase order report
    """,
    "author": "Solvos",
    "license": "LGPL-3",
    "version": "13.0.1.0.0",
    'category': "Operations/Purchase",
    "website": "https://github.com/solvosci/slv-purchase",
    "depends": [
        "purchase",
    ],
    "data": [
        "reports/purchase_order_report.xml"
    ],
    'installable': True,
}
