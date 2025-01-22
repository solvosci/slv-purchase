# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3.0 (https://www.gnu.org/licenses/lgpl-3.0.html)

from odoo import models, _
from odoo.exceptions import UserError


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    def copy_pol(self):
        for line in self:
            if line.order_id.state in ["cancel", "done"]:
                raise UserError(_("You cannot copy lines from a canceled or locked purchase order."))
            line.copy(default={'order_id': line.order_id.id})
