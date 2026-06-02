# © 2026 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html
{
    "name": "Purchase Stock - Update product standard price from purchases",
    "summary": """
        For product category set as standard price cost method, enables
        automatic updating for product costs, based on last purchase price
    """,
    "author": "Solvos",
    "license": "LGPL-3",
    "version": "15.0.1.0.1",
    "category": "Inventory/Purchase",
    "website": "https://github.com/solvosci/slv-purchase",
    "depends": ["purchase_stock"],
    "data": ["views/product_category_views.xml"],
    "installable": True,
}
