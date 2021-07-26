# © 2021 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

from odoo import api, fields, models


class AccountMove(models.Model):
    _inherit = "account.move"

    purchase_type_id = fields.Many2one(
        comodel_name="purchase.order.type",
        string="Purchase Type",
        compute="_compute_purchase_type_id",
        store=True,
        readonly=False,
        states={"posted": [("readonly", True)], "cancel": [("readonly", True)]},
        copy=True,
    )

    @api.depends("partner_id", "company_id")
    def _compute_purchase_type_id(self):
        self.purchase_type_id = self.env["purchase.order.type"]
        for record in self.filtered(
            lambda am: am.type in ["in_invoice", "in_refund"]
        ):
            if not record.partner_id:
                record.purchase_type_id = self.env["purchase.order.type"].search(
                    [("company_id", "in", [self.env.company.id, False])], limit=1
                )
            else:
                purchase_type = (
                    record.partner_id.with_context(
                        force_company=record.company_id.id
                    ).purchase_type
                    or record.partner_id.commercial_partner_id.with_context(
                        force_company=record.company_id.id
                    ).purchase_type
                )
                if purchase_type:
                    record.purchase_type_id = purchase_type

    @api.onchange("purchase_type_id")
    def onchange_purchase_type_id(self):
        if self.purchase_type_id.payment_term_id:
            self.invoice_payment_term_id = self.purchase_type_id.payment_term_id.id
        if self.purchase_type_id.journal_id:
            self.journal_id = self.purchase_type_id.journal_id.id
