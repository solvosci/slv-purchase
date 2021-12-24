# © 2021 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

from odoo import api, fields, models


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    picking_last_date_done = fields.Date(
        compute="_compute_picking_last_date_done",
        help="Technical field for Purchase Due Date calculation",
        store=True,
        readonly=True,
    )

    purchase_date_due = fields.Date(
        compute="_compute_purchase_date_due",
        store=True,
        readonly=True,
    )

    @api.depends("picking_ids.date_done")
    def _compute_picking_last_date_done(self):
        for purchase in self:
            pickings_done = purchase.picking_ids.filtered(
                lambda x: x.state == "done" and x.date_done
            ).sorted("date_done")
            purchase.picking_last_date_done = (
                pickings_done and
                pickings_done[-1].date_done
            )

    @api.depends("payment_term_id", "picking_last_date_done")
    def _compute_purchase_date_due(self):
        for purchase in self:
            purchase.purchase_date_due = (
                purchase.payment_term_id and
                purchase.picking_last_date_done and
                purchase.payment_term_id._compute_for_purchase(
                    purchase.amount_total,
                    date_ref=purchase.picking_last_date_done,
                    currency=purchase.currency_id
                )
            )
