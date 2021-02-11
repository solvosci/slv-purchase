# © 2021 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html
{
    "name": "Purchase Order Product Summary",
    "summary": """
        Adds to purchase report a new section
        with the grouped products and their total.
    """,
    "author": "Solvos",
    "license": "LGPL-3",
    "version": "13.0.1.0.0",
    'category': "Operations/Purchase",
    "website": "https://github.com/solvosci/slv-stock",
    "depends": [
        "purchase",
    ],
    "data": [
        "report/purchase_order_summary_report.xml",
        "report/purchase_order_summary_template.xml",
    ],
    'installable': True,
}
