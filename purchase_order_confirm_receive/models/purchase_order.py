# © 2022 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html
from odoo import models


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    def action_batch_confirm_receive(self):
        for order in self.browse(self.env.context["active_ids"]):
            order.button_confirm_receive()

    def button_confirm_receive(self):
        if self.state in ("draft", "sent"):
            self.button_confirm()
        self._action_receive()

    def _action_receive(self):
        pickings = self.picking_ids.filtered(
            lambda x: x.state == "assigned"
        )
        if pickings:
            itwiz = self.env["stock.immediate.transfer"].create({
                "pick_ids": [(6, False, pickings.ids)]
            })
            itwiz.process()
