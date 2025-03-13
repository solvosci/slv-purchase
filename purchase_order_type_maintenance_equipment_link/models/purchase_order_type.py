# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import models, fields


class PurchaseOrderType(models.Model):
    _inherit = 'purchase.order.type'

    use_maintenance_equipment = fields.Boolean(default=False)
