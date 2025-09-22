# © 2021 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import api, models

import ast


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    @api.onchange("order_type")
    def onchange_order_type(self):
        super().onchange_order_type()
        for order in self:
            if order.order_type.picking_type_id:
                order.picking_type_id = order.order_type.picking_type_id
            if order.order_type.analytic_account_id:
                order.order_line.write({
                    "analytic_distribution": {
                        order.order_type.analytic_account_id.id: 100
                    },
                })

    def _prepare_invoice(self):
        invoice_vals = super()._prepare_invoice()
        values = {}
        if self.order_type:
            values["purchase_type_id"] = self.order_type.id
        if self.order_type.journal_id:
            values["journal_id"] = self.order_type.journal_id.id

        invoice_vals.update(values)

        return invoice_vals

    def action_view_invoice(self, invoices=False):
        result = super().action_view_invoice(invoices=invoices)
        purchase_types = self.order_type
        if len(purchase_types) == 1:
            result.setdefault("context", {})
            if isinstance(result.get("context"), str):
                result["context"] = ast.literal_eval(result["context"])
            result["context"]["default_purchase_type_id"] = purchase_types.id
        return result
