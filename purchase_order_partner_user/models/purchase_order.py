# © 2021 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

from odoo import api, models


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    @api.onchange("partner_id")
    def onchange_partner_user_id(self):
        self.ensure_one()
        if self.partner_id.user_id:
            self.user_id = self.partner_id.user_id
        else:
            self.user_id = self.env.user
