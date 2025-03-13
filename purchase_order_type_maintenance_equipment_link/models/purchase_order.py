# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import models, fields, api


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    show_maintenance_equipment = fields.Boolean(
        related="order_type.use_maintenance_equipment",
        store=True,
    )

    @api.onchange('show_maintenance_equipment')
    def _onchange_show_maintenance_equipment(self):
        for record in self:
            if not record.show_maintenance_equipment:
                record.maintenance_equipment_default_id = False
                for order_line in record.order_line:
                    order_line.maintenance_equipment_ids = False
