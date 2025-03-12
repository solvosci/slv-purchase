# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3.0 (https://www.gnu.org/licenses/agpl-3.0.html)
{
    "name": "Purchase Order Maintenance Equipment Link",
    "summary": """
        Link purchase orders to maintenance equipment 
        and restrict products based on them.
    """,
    "author": "Solvos",
    "license": "AGPL-3",
    "version": "13.0.1.0.0",
    "category": "Purchases",
    "website": "https://github.com/solvosci/slv-purchase",
    "depends": [
        "base_view_inheritance_extension",
        "purchase",
        "product_maintenance_equipment_link"
    ],
    "data": [
        "views/purchase_order_views.xml",
        "views/maintenance_equipment_views.xml",
    ],

}
