# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3.0 (https://www.gnu.org/licenses/lgpl-3.0.html)
{
    "name": "Purchase Invoice - Currency Custom Rate",
    "summary": """
        Allows you to send rate values from a purchase when the invoice is issued in a currency other than the primary currency.
    """,
    "version": "13.0.1.0.0",
    "category": "Accounting & Finance",
    "website": "https://github.com/solvosci/slv-account",
    "author": "Solvos",
    "license": "LGPL-3",
    "depends": [
        "purchase",
        "account_invoice_currency_custom_rate",
    ],
    "data": ["views/purchase_order_views.xml"],
    "installable": True,
}
