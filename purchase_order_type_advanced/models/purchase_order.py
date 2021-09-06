# © 2021 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

from odoo import api, fields, models


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    pricelist_id = fields.Many2one(
        comodel_name="product.pricelist",
        strint="Pricelist"
    )

    @api.onchange("order_type")
    def onchange_order_type(self):
        super().onchange_order_type()
        for order in self:
            if order.order_type.picking_type_id:
                order.picking_type_id = order.order_type.picking_type_id
            if order.order_type.pricelist_id:
                order.pricelist_id = order.order_type.pricelist_id

    def action_view_invoice(self):
        res = super(PurchaseOrder, self).action_view_invoice()
        ctx = {}
        if self.order_type.journal_id:
            ctx["default_journal_id"] = self.order_type.journal_id.id
        if self.order_type:
            ctx["default_purchase_type_id"] = self.order_type.id
        res["context"].update(ctx)
        return res
