# © 2022 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html
{
    "name": "Purchase Order Report - RFQ style",
    "summary": """
        Adds a new Purchase Order report based on Purchase RFQ template
    """,
    "author": "Solvos",
    "license": "LGPL-3",
    "version": "14.0.1.0.0",
    'category': "Inventory/Purchase",
    "website": "https://github.com/solvosci/slv-purchase",
    "depends": ["purchase"],
    "data": [
        "report/purchase_order_report.xml",
        "report/purchase_order_report_templates.xml",
    ],
    'installable': True,
}
