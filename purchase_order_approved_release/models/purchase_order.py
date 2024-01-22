# © 2024 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import models


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"
    
    def _approval_allowed(self):
        ret = super()._approval_allowed()
        if self.env.context.get("skip_approval_allowed_release", False):
            return ret or self.user_has_groups("purchase.group_purchase_user")
        return ret

    def button_release(self):
        br_obj = self.with_context(skip_approval_allowed_release=True)
        return super(PurchaseOrder, br_obj).button_approve()
