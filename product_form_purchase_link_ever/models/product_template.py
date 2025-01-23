# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import models, fields
from odoo.tools.float_utils import float_round


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    purchased_ever_product_qty = fields.Float(compute="_compute_purchased_ever_product_qty")

    def _compute_purchased_ever_product_qty(self):
        for template in self:
            template.purchased_ever_product_qty = float_round(sum([p.purchased_ever_product_qty for p in template.product_variant_ids]), precision_rounding=template.uom_id.rounding)
