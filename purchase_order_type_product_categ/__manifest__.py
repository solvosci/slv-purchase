# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
{
    "name": "Purchase Order Type Product Category",
    "summary": """
        Adds new field and filters to the product that depend on the product category in the purchase order types.
    """,
    "author": "Solvos",
    "license": "AGPL-3",
    "version": "13.0.1.0.0",
    'category': "Operations/Purchase",
    "website": "https://github.com/solvosci/slv-purchase",
    "depends": [
        "purchase_order_type",
        "base_view_inheritance_extension",
    ],
    "data": [
        "views/purchase_order_views.xml",
        "views/purchase_order_type_views.xml"
    ],
    'installable': True,
}
