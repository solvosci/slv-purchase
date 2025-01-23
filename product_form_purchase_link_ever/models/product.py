# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import models, fields
from odoo.tools.float_utils import float_round


class ProductProduct(models.Model):
    _inherit = 'product.product'

    purchased_ever_product_qty = fields.Float(compute="_compute_purchased_ever_product_qty")

    def _compute_purchased_ever_product_qty(self):
        domain = [
            ('order_id.state', 'in', ['purchase', 'done']),
            ('product_id', 'in', self.ids),
        ]
        order_lines = self.env['purchase.order.line'].read_group(domain, ['product_id', 'product_uom_qty'], ['product_id'])
        purchased_data = dict([(data['product_id'][0], data['product_uom_qty']) for data in order_lines])
        for product in self:
            if not product.id:
                product.purchased_ever_product_qty = 0.0
                continue
            product.purchased_ever_product_qty = float_round(purchased_data.get(product.id, 0), precision_rounding=product.uom_id.rounding)
