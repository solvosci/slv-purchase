# © 2024 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3.0 (http://www.gnu.org/licenses/agpl-3.0.html)

from odoo import models, api


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    def action_view_invoice(self):
        res = super(PurchaseOrder, self).action_view_invoice()
        ctx = {}
        if self.payment_mode_id:
            ctx["default_payment_mode_id"] = self.payment_mode_id.id
        res["context"].update(ctx)
        return res