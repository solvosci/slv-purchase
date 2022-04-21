# © 2022 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html
{
    "name": "Purchase Order Move Menu - Link to Stock Picking Move Weight",
    "summary": """
        Adds related order to Purchase Move views
    """,
    "author": "Solvos",
    "license": "LGPL-3",
    "version": "13.0.1.0.0",
    "category": "Operations/Purchase",
    "website": "https://github.com/solvosci/slv-purchase",
    "depends": [
        "purchase_order_move_menu",
        "stock_picking_mgmt_weight",
    ],
    "data": [
        "views/stock_move_views.xml",
    ],
    'installable': True,
}
