# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3.0 (https://www.gnu.org/licenses/lgpl-3.0.html)

from odoo import fields, models, api


class StockMove(models.Model):
    _inherit = "stock.move"

    po_menu_exclude = fields.Boolean(
        related='purchase_order.order_type.stock_move_menu_exclude',
        string='Excluded for PO moves menu',
        store=True,
    )

    @api.model
    def action_purchase_moves(self):
        res = super(StockMove, self).action_purchase_moves()
        res["domain"] = "[%s, ('po_menu_exclude', '=', False)]" % res["domain"][1:-1]
        return res
