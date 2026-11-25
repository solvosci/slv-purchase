# © 2026 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3.0 (https://www.gnu.org/licenses/lgpl-3.0.html)
{
    "name": "Purchase Line Transport Mode",
    "summary": "Indicate SEA / AIR for each purchase order line and display it on the PDF",
    "version": "19.0.1.0.0",
    "category": "Purchase",
    "author": "Solvos",
    "website": "https://github.com/solvosci/slv-purchase",
    "license": "LGPL-3",
    "depends": ["purchase"],
    "data": [
        "views/purchase_order_views.xml",
        "report/purchase_reports.xml",
    ],
    "installable": True,
}
