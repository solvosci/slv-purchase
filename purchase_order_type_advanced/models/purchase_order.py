# © 2021 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

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

    def _prepare_invoice(self):
        invoice_vals = super()._prepare_invoice()
        invoice_vals["purchase_type_id"] = self.order_type.id
        if self.order_type.journal_id:
            invoice_vals["journal_id"] = self.order_type.journal_id.id 
        return invoice_vals

    def action_view_invoice(self, invoices=False):
        res = super().action_view_invoice(invoices=invoices)
        ctx = ast.literal_eval(res.get("context", "{}"))
        if invoices:
            # Batch invoice creation: first invoice rules for extra default
            #  values in case of later new invoice creation
            ctx.update({
                "default_journal_id": invoices[0].journal_id.id or False,
                "default_purchase_type_id": invoices[0].purchase_type_id.id or False,
            })
        else:
            if self.order_type.journal_id:
                ctx["default_journal_id"] = self.order_type.journal_id.id
            if self.order_type:
                ctx["default_purchase_type_id"] = self.order_type.id
        res["context"] = str(ctx)
        return res
