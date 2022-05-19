# © 2022 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3.0 (https://www.gnu.org/licenses/lgpl-3.0.html)

from odoo import fields, models


class StockMove(models.Model):
    _inherit = "stock.move"

    po_product_categ_id = fields.Many2one(related="product_id.categ_id")
    po_currency_id = fields.Many2one(related="purchase_line_id.currency_id")
    purchase_order = fields.Many2one(
        related="purchase_line_id.order_id",
        store=True,
    )
    purchase_partner_id = fields.Many2one(
        related="purchase_order.partner_id",
        store=True,
    )
    purchase_user_id = fields.Many2one(
        related="purchase_line_id.order_id.user_id",
    )
