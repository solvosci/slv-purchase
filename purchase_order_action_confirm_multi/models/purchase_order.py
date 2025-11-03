# © 2022 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

from odoo import models


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    def action_purchase_order_confirm_multi(self):
        for record in self.browse(self.env.context['active_ids']).filtered(lambda x: x.state in ('draft', 'sent')):
            if not record.payment_term_id:
                record.onchange_partner_id()
            record.button_confirm()
