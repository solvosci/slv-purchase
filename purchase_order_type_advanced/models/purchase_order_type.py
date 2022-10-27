# © 2021 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

from odoo import _, fields, models
from odoo.exceptions import ValidationError


class PurchaseOrderType(models.Model):
    _inherit = "purchase.order.type"

    journal_id = fields.Many2one(
        comodel_name="account.journal",
        string="Billing Journal",
        domain=[("type", "=", "purchase")],
    )
    picking_type_id = fields.Many2one(
        comodel_name='stock.picking.type',
        string='Deliver To'
    )

    def write(self, values):
        """
        Prevent non-coherence between default Deliver To for a Purchase Order
        Type and default Automatic Purchases Purchase Order Type for a
        Picking Type
        """
        spt = (
            values.get("picking_type_id", False)
            and self.env["stock.picking.type"].browse(values.get("picking_type_id"))
            or False
        )
        if spt:
            pot_ids = self.filtered(lambda x: x.picking_type_id)
            affected_spts = self.env["stock.picking.type"].search(
                [("buy_purchase_order_type_id", "in", pot_ids.ids)]
            )
            if affected_spts:
                pot_names = ", ".join(pot_ids.mapped("name"))
                spt_names = ", ".join(affected_spts.mapped("name"))
                raise ValidationError(_(
                    "Cannot change Deliver To data because the Purchase Order"
                    " Type(s) [%s] is/are used in Stock Picking Type(s) [%s]"
                    " as default purchase type for automatic purchases"
                ) % (pot_names, spt_names))
        return super().write(values)
