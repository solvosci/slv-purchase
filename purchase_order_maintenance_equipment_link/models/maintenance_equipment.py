# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import models, fields, _


class MaintenanceEquipment(models.Model):
    _inherit = 'maintenance.equipment'

    purchase_order_count = fields.Integer(compute='_compute_purchase_orders')
    purchase_order_ids = fields.Many2many(
        comodel_name='purchase.order',
        compute='_compute_purchase_orders',
    )

    def _compute_purchase_orders(self):
        for equipment in self:
            purchase_orders = self.env['purchase.order.line'].search([
                ('state', 'in', ['purchase', 'done']),
                ('maintenance_equipment_ids', 'in', equipment.id),
            ]).order_id
            equipment.purchase_order_ids = purchase_orders
            equipment.purchase_order_count = len(purchase_orders)

    def action_view_purchase_order(self):
        action = {
            'name': _('Purchase Orders'),
            'res_model': 'purchase.order',
            'type': 'ir.actions.act_window',
            'context':{},
            'domain': [('id', "in", self.purchase_order_ids.ids)]
        }
        
        if self.purchase_order_count == 1:
            action['view_mode'] = 'form'
            action['res_id'] = self.purchase_order_ids.id
        else:
            action['view_mode'] = 'tree,form'
        return action
