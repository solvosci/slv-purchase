# © 2024 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

from odoo import models, fields, api


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    sale_partner_id = fields.Many2one("res.partner", compute="_compute_sale_partner_id", store=True, readonly=False)

    @api.depends("order_line.sale_order_id.partner_id") 
    def _compute_sale_partner_id(self):
        for order in self:
            partner_id = order.order_line.sale_order_id.partner_id
            if len(partner_id) == 1:
                order.sale_partner_id = partner_id
            elif len(partner_id) > 1:
                order.sale_partner_id = False
