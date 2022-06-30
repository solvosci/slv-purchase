# © 2022 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html
{
    "name": "Purchase Order Line - Custom LoW Code",
    "summary": """
        Adds a custom LoW Code for order lines
    """,
    "author": "Solvos",
    "license": "LGPL-3",
    "version": "13.0.1.1.0",
    'category': "Operations/Purchase",
    "website": "https://github.com/solvosci/slv-purchase",
    "depends": ["purchase", "base_waste_mgmt_data"],
    "data": [
        "views/purchase_order_views.xml"
    ],
    'installable': True,
}
