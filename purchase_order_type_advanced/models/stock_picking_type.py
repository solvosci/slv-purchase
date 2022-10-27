# © 2022 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

from odoo import fields, models


class StockPickingType(models.Model):
    _inherit = "stock.picking.type"

    buy_purchase_order_type_id = fields.Many2one(
        comodel_name="purchase.order.type",
        string="Order type for automatic purchases",
    )
