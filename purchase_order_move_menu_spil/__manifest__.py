# © 2022 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
{
    "name": "Purchase Order Move Menu - Link to Invoices",
    "summary": """
        Adds invoice data (such as invoice date) to purchase related moves menu
    """,
    "author": "Solvos",
    "license": "AGPL-3",
    "version": "13.0.1.0.1",
    "category": "Purchase",
    "website": "https://github.com/solvosci/slv-purchase",
    "depends": [
        "purchase_order_move_menu",
        "stock_picking_invoice_link",
        "purchase_stock_picking_invoice_link",
        "web_tree_dynamic_colored_field"
    ],
    "data": [
        "views/stock_move_views.xml",
    ],
    'installable': True,
}
