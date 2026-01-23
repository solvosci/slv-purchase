# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html
{
    "name": "Purchase Order Move Menu - Link to Purchase Order Type",
    "summary": """
        Adds related order to Purchase Order Type
    """,
    "author": "Solvos",
    "license": "LGPL-3",
    "version": "17.0.1.0.0",
    "category": "Operations/Purchase",
    "website": "https://github.com/solvosci/slv-purchase",
    "depends": [
        "purchase_order_move_menu",
        "purchase_order_type"
    ],
    "data": [
        "views/purchase_order_type_views.xml",
    ],
    "installable": True,
    "pre_init_hook": "pre_init_hook",
}
