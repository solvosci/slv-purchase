# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3.0 (https://www.gnu.org/licenses/agpl-3.0.html)
{
    "name": "Purchase Order Type Maintenance Equipment Link",
    "summary": """
        Controls the visibility of maintenanc _equipments 
        in purchase order lines based on the purchase order type.
    """,
    "author": "Solvos",
    "license": "AGPL-3",
    "version": "13.0.1.0.0",
    "category": "Purchases",
    "website": "https://github.com/solvosci/slv-purchase",
    "depends": [
        "purchase_order_maintenance_equipment_link",
        "purchase_order_type"
    ],
    "data": [
        "views/purchase_order_type_views.xml",
        "views/purchase_order_views.xml",
    ],

}
