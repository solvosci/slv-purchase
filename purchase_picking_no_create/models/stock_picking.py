# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, _


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    def copy(self, default=None):
        ctx = dict(self.env.context)
        if self.purchase_id:
            ctx.update(disable_picking_create = _("You cannot manually create Stock Picking from a Purchase Order."))
        return super(StockPicking, self.with_context(ctx)).copy(default)
