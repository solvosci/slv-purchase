# © 2021 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

from odoo import api, fields, models


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
                    "account_analytic_id": order.order_type.analytic_account_id.id,
                })

    @api.onchange("partner_id")
    def onchange_partner_id(self):
        """
        When partner changes, if current payment term matches with current selection
        and at order type and it's marked as priority, it will be preserved
        """
        old_payment_term_id = self.payment_term_id
        preserve_payment = False
        if (
            old_payment_term_id
            and self.order_type.payment_term_prioritary
            and old_payment_term_id == self.order_type.payment_term_id
        ):
            preserve_payment = True
        res = super(PurchaseOrder, self).onchange_partner_id()
        if preserve_payment and old_payment_term_id != self.payment_term_id:
            self.payment_term_id = old_payment_term_id
        return res

    def action_view_invoice(self):
        res = super(PurchaseOrder, self).action_view_invoice()
        ctx = {}
        if self.order_type.journal_id:
            ctx["default_journal_id"] = self.order_type.journal_id.id
        if self.order_type:
            ctx["default_purchase_type_id"] = self.order_type.id
        res["context"].update(ctx)
        return res
