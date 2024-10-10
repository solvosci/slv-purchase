# © 2024 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
{
    "name": "Stock Warehouse Analytic Purchase",
    "summary": """
        Adds analytical fields to lines based on the related warehouse operation type, 
        this new definition has a higher priority than "Analytic Defaults Rules"
    """,
    "author": "Solvos",
    "license": "AGPL-3",
    "version": "14.0.1.0.1",
    "category": "Inventory/Purchase",
    "website": "https://github.com/solvosci/slv-purchase",
    "depends": ["stock_warehouse_analytic"],
    'installable': True,
}
