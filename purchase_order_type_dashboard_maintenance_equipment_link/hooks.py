# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

from odoo import SUPERUSER_ID, api


def uninstall_hook(cr, registry, vals=None):
    env = api.Environment(cr, SUPERUSER_ID, {})
    env.ref("purchase_order_type_dashboard.purchase_order_dashboard_menu").action = env.ref("purchase_order_type_dashboard.purchase_order_type_dashboard_action")
