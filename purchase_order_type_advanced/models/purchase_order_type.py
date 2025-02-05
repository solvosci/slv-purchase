# © 2021 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

from odoo import api, fields, models


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
    analytic_account_id = fields.Many2one(
        comodel_name="account.analytic.account",
        string="Analytic account",
        check_company=True,
    )

    payment_term_prioritary = fields.Boolean(
        string="Is Payment Term Prioritary",
        compute="_compute_payment_term_prioritary",
        store=True,
        readonly=False,
        default=False,
    )

    @api.depends("payment_term_id")
    def _compute_payment_term_prioritary(self):
        self.filtered(lambda x: not x.payment_term_id).update({
            "payment_term_prioritary": False,
        })
