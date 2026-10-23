# © 2026 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html
{
    "name": "Purchase Order Report Hide Discount",
    "summary": """
        Hides the discount column in purchase order reports
    """,
    "author": "Solvos",
    "license": "LGPL-3",
    "version": "17.0.1.0.0",
    'category': "Operations/Purchase",
    "website": "https://github.com/solvosci/slv-purchase",
    "depends": ["purchase"],
    "data": [
        "reports/report_purchase_order.xml"
    ],
    'installable': True,
}
