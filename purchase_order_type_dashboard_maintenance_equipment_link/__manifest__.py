# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3.0 (https://www.gnu.org/licenses/agpl-3.0.html)
{
    "name": "Purchase Order Type Dashboard Maintenance Equipment Link",
    "summary": """
        Submenus ‘General Orders’ and Maintenance Orders added in the menu ‘Dashboard’.
        'General orders’ shows those types of orders where maintenance equipment are NOT used.
        ‘Maintenance orders’ shows those types of orders where maintenance equipment are used.
    """,
    "author": "Solvos",
    "license": "AGPL-3",
    "version": "17.0.1.0.0",
    "category": "Purchases",
    "website": "https://github.com/solvosci/slv-purchase",
    "depends": [
        "purchase_order_type_maintenance_equipment_link",
        "purchase_order_type_dashboard",
    ],
    "data": [
        "views/menu_purchase_order.xml",
    ],
    "installable": True,
    "uninstall_hook": "uninstall_hook",
}
