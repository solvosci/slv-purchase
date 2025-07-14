# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, _

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    def action_view_picking(self):
        action = super(PurchaseOrder, self).action_view_picking()
        action['context'] = dict(action.get('context', {}))
        action['context']['disable_picking_create'] = _("You cannot manually create Stock Picking from a Purchase Order.")
        action['context']['disable_move_create'] = _("You cannot manually create Stock Move from a Purchase Order.")
        return action
