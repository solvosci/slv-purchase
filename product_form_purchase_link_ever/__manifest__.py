# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
{
    "name": "Product Form Purchase Link Ever",
    "summary": """
        Shows the total purchases since ever instead of the last year.
    """,
    "author": "Solvos",
    "license": "AGPL-3",
    "version": "15.0.1.0.0",
    "category": "Inventory/Purchase",
    "website": "https://github.com/solvosci/slv-purchase",
    "depends": [
        "product_form_purchase_link",
    ],
    "data": [
        "views/product_template_views.xml",
        "views/product_product_views.xml",
    ],
    'installable': True,
}
