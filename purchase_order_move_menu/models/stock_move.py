# © 2022 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3.0 (https://www.gnu.org/licenses/lgpl-3.0.html)

from odoo import api, fields, models


class StockMove(models.Model):
    _inherit = "stock.move"

    po_product_categ_id = fields.Many2one(related="product_id.categ_id")
    po_currency_id = fields.Many2one(related="purchase_line_id.currency_id")
    purchase_order = fields.Many2one(
        related="purchase_line_id.order_id",
        store=True,
    )
    purchase_partner_id = fields.Many2one(
        related="purchase_order.partner_id",
        store=True,
    )
    purchase_user_id = fields.Many2one(
        related="purchase_line_id.order_id.user_id",
    )

    @api.model
    def action_purchase_moves(self):
        """
        Modifies original purchase stock move action depending on Purchase
        role of the logged user
        """
        # Alternative development: making our own action from scatch, like
        #  https://github.com/odoo/odoo/blob/13.0/addons/stock/models/stock_quant.py#L622
        # The selected strategy allow us to define action in XML file,
        #  but has the problem of the needed "fake zero results domain" in
        #  order to prevent "F5" pages reload, that should only use the
        #  original action definition
        action = self.env.ref(
            "purchase_order_move_menu.action_stock_move_po_move_menu"
        )
        result = action.read()[0]
        # Default (fake) domain is replaced with the right one
        domain_str = "('purchase_line_id','!=', False), ('state','=', 'done')"
        if not self._check_purchase_all_permissions(self.env.user):
            domain_str += ", ('purchase_user_id','=',%d)" % self.env.user.id
        result["domain"] = "[%s]" % domain_str

        return result

    @api.model
    def _check_purchase_all_permissions(self, user):
        return user.has_group("purchase.group_purchase_manager")
