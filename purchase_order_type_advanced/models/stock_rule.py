# © 2022 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

from odoo import models


class StockRule(models.Model):
    _inherit = "stock.rule"

    def _prepare_purchase_order(self, company_id, origins, values):
        ret = super()._prepare_purchase_order(company_id, origins, values)
        purchase_order_type = self.env["stock.picking.type"].sudo().browse(
            ret["picking_type_id"]
        ).buy_purchase_order_type_id
        if purchase_order_type:
            ret.update({
                "order_type": purchase_order_type.id,
                "incoterm_id": purchase_order_type.incoterm_id.id,
            })
            ret.setdefault(
                "payment_term_id", purchase_order_type.payment_term_id.id
            )
        return ret
