# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html


def uninstall_hook(env):
    env.ref("purchase_order_type_dashboard.purchase_order_dashboard_menu").action = env.ref("purchase_order_type_dashboard.purchase_order_type_dashboard_action")
