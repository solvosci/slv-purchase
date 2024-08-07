# © 2024 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

from odoo import models, api


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    @api.depends(
        "order_line.move_dest_ids.group_id.sale_id.partner_id",
        "order_line.move_ids.move_dest_ids.group_id.sale_id.partner_id",
    )
    def _compute_sale_partner_id(self):
        for order in self:
            super(PurchaseOrder, order)._compute_sale_partner_id()            
            partner_id = (
                order.order_line.move_dest_ids.group_id.sale_id.partner_id
                | order.order_line.move_ids.move_dest_ids.group_id.sale_id.partner_id
                | order.sale_partner_id
            )
            if len(partner_id) == 1 and not order.sale_partner_id:
                order.sale_partner_id = partner_id
            elif len(partner_id) > 1:
                order.sale_partner_id = False
