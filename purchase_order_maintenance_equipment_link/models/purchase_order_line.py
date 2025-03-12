# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import models, fields, api


class PurchaseOrderLine(models.Model):
    _inherit="purchase.order.line"

    maintenance_equipment_ids = fields.Many2many('maintenance.equipment')

    @api.onchange('product_id')
    def _onchange_product_id(self):
        if self.order_id and self.order_id.maintenance_equipment_default_id and not self.maintenance_equipment_ids and not self.product_id:
            self.maintenance_equipment_ids = [(4, self.order_id.maintenance_equipment_default_id.id)]
