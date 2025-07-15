# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Purchase Picking No Create",
    "summary": """
        Disables the creation of stock pickings and moves from the Purchase Order "Pickings" button.
    """,
    "author": "Solvos",
    "license": "AGPL-3",
    "version": "13.0.1.0.0",
    "category": "Purchase",
    "website": "https://github.com/solvosci/slv-purchase",
    "depends": [
        "purchase_stock",
        "stock_picking_no_create_base",
    ],
    "installable": True,
}
