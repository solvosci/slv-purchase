# © 2026 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

from odoo import _, models
from odoo.tools import float_compare


class StockMove(models.Model):
    _inherit = "stock.move"

    def _action_done(self, cancel_backorder=False):
        moves = super()._action_done(cancel_backorder=cancel_backorder)
        # Super call ensures that every move to be processed is already at
        # 'done' state. And we only take care of original primary validated
        # moves that come from a purchase, not returned ones (outgoing), or
        # even N-incoming (eg. a return from a return)
        precision = self.env["decimal.precision"].precision_get("Product Price")
        moves_upd_price = moves.filtered(
            lambda x: (
                x.purchase_line_id
                and not x.origin_returned_move_id
                and x.product_id.with_company(
                    x.company_id
                ).categ_id.property_cm_standard_auto_upd
                and float_compare(
                    x.product_id.with_company(
                        x.company_id
                    ).standard_price,
                    x.price_unit,
                    precision_digits=precision
                ) != 0
            )
        )
        # TODO improve this, the same product could be called twice or 
        # even more times. You should keep only one move by product and company
        for move in moves_upd_price:
            product = move.product_id.with_company(
                move.company_id
            )
            product.standard_price = move.price_unit
            post_message = _(
                "Product price at %s have been set according to %s purchase order stock incoming",
                move.company_id.name,
                move.purchase_line_id.order_id.name
            )
            product.message_post(body=post_message)
            if product.product_tmpl_id.product_variant_count == 1:
                product.product_tmpl_id.message_post(body=post_message)

        return moves
