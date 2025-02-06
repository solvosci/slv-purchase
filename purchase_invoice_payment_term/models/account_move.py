# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3.0 (http://www.gnu.org/licenses/lgpl-3.0.html)

from odoo import models, api

class AccountMove(models.Model):
    _inherit = 'account.move'

    @api.onchange('partner_id')
    def _onchange_partner_id(self):
        purchase_payment_term = self.invoice_payment_term_id if self.invoice_payment_term_id else False
        res = super(AccountMove, self)._onchange_partner_id()
        if self.purchase_id and purchase_payment_term and purchase_payment_term != self.invoice_payment_term_id:
            self.invoice_payment_term_id = purchase_payment_term
        return res
