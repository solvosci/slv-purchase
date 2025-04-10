# © 2024 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3.0 (http://www.gnu.org/licenses/agpl-3.0.html)

from odoo import models, api


class AccountMove(models.Model):
    _inherit = "account.move"

    @api.depends("partner_id", "company_id")
    def _compute_payment_mode(self):
        super()._compute_payment_mode()
        for move in self.filtered(lambda x: x.partner_id and x.type == "in_invoice"):
            move.payment_mode_id = move.purchase_id.payment_mode_id
