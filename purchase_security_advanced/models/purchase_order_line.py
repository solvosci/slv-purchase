# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import models


class PurchaseOrderLine(models.Model):
    _inherit = "purchase.order.line"

    def _suggest_quantity(self):
        # This will look for sellers (partners), that couldn't be directly
        #  accessed by some users. Then, permssions must be bypassed
        self_sudo = self.sudo()
        super(PurchaseOrderLine, self_sudo)._suggest_quantity()
