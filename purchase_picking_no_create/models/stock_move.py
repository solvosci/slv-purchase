# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, api, _


class StockMove(models.Model):
    _inherit = 'stock.move'

    @api.model_create_multi
    def create(self, vals_list):
        ctx = dict(self.env.context)
        for record in vals_list:
            if self.picking_id.browse(record.get('picking_id')).exists().purchase_id and not record.get('purchase_line_id'):
                ctx.update(disable_move_create = _("You cannot manually create Stock Move from a Purchase Order."))
        return super(StockMove, self.with_context(ctx)).create(vals_list)
