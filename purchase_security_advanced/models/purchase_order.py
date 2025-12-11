# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import models


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    def _add_supplier_to_product(self):
        # This will look for sellers (partners), that couldn't be directly
        #  accessed by some users. Then, permssions must be bypassed
        order_obj = self.with_context(skip_sellers_permissions=True)
        super(PurchaseOrder, order_obj)._add_supplier_to_product()
