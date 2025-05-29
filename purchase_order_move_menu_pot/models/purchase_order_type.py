# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3.0 (https://www.gnu.org/licenses/lgpl-3.0.html)

from odoo import fields, models


class PurchaseOrderType(models.Model):
    _inherit = "purchase.order.type"

    stock_move_menu_exclude = fields.Boolean()
