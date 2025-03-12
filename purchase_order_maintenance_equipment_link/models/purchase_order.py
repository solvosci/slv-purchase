# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import models, fields


class PurchaseOrder(models.Model):
    _inherit="purchase.order"

    maintenance_equipment_default_id = fields.Many2one(
        'maintenance.equipment',
        string='Default Maint. Equip.')
