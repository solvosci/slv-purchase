# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import fields, models


class PurchaseOrderType(models.Model):
    _inherit = 'purchase.order.type'

    product_category_id = fields.Many2one(
        'product.category',
        help='''if filled, orders for this type will only be able to 
            select products that belong to this category hierarchy''',
    )
