# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3.0 (https://www.gnu.org/licenses/lgpl-3.0.html)

from odoo import api, models, fields


class PurchaseOrder(models.Model):
    _name = "purchase.order"
    _inherit = ["purchase.order", "currency.custom.rate.mixin"]

    def _prepare_invoice(self):
        res = super()._prepare_invoice()
        res.update(self._prepare_invoice_custom_rate_vals())
        return res
