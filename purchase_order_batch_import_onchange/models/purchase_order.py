# © 2021 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html
from odoo import models


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    def action_batch_import_onchange(self):
        for record in self.browse(self.env.context["active_ids"]):
            record.action_import_onchange()

    def action_import_onchange(self):
        self.ensure_one()
        # From odoo/purchase addon
        self.onchange_partner_id()
        # From solvosci/purchase_order_partner_user addon
        self.onchange_partner_user_id()
        # From OCA/purchase_order_type addon
        self.onchange_order_type()
        # From odoo/purchase addon
        self._compute_tax_id()
