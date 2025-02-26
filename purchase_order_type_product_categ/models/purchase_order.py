# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import fields, models,api


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    allowed_product_categ_ids = fields.Many2many(
        'product.category',
        compute='_compute_allowed_product_categ_ids',
    )

    @api.depends('order_type.product_category_id')
    def _compute_allowed_product_categ_ids(self):
        product_categ_obj = self.env['product.category']
        for record in self:
            domain = [('id', 'child_of', record.order_type.product_category_id.id)] if record.order_type.product_category_id else []
            record.allowed_product_categ_ids = product_categ_obj.search(domain)
