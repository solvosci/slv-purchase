# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3.0 (https://www.gnu.org/licenses/lgpl-3.0.html)

from odoo import models
from odoo.tools import float_is_zero


class PurchaseOrderLine(models.Model):
    _inherit = "purchase.order.line"

    def _compute_price_unit_and_date_planned_and_name(self):
        precision_price = self.env['decimal.precision'].precision_get('Product Price')
        save_values = {
            line: {'price_unit': line.price_unit, 'discount': line.discount}
            for line in self if not float_is_zero(line.price_unit, precision_digits=precision_price)
        }
        super()._compute_price_unit_and_date_planned_and_name()
        for line, values in save_values.items():
            line.price_unit = values['price_unit']
            line.discount = values['discount']
