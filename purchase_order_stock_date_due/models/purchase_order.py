# © 2021 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

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
            purchase.purchase_date_due = False
            if purchase.payment_term_id and purchase.picking_last_date_done:
                pay_term = purchase.payment_term_id._compute_terms(
                    date_ref=purchase.picking_last_date_done,
                    currency=purchase.currency_id,
                    company=purchase.company_id,
                    tax_amount=purchase.amount_tax or 0,
                    tax_amount_currency=purchase.amount_tax or 0,
                    sign=1,
                    untaxed_amount=purchase.amount_untaxed,
                    untaxed_amount_currency=purchase.amount_untaxed,
                )
                dates = [line.get("date") for line in pay_term.get("line_ids")]

                if dates:
                    purchase.purchase_date_due = max(dates)
