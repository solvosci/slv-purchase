# © 2023 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

from odoo import api, fields, models

class AccountAnalyticAccount(models.Model):
    _inherit = "stock.move.line"

    po_account_analytic_id = fields.Many2one('account.analytic.account',
        string="PO Analytic Account",
        compute="_compute_po_account_analytic_id",
        store=True)

    @api.multi
    @api.depends('move_id.purchase_line_id.account_analytic_id')
    def _compute_po_account_analytic_id(self):
        for record in self:
            record.po_account_analytic_id = record.move_id.purchase_line_id.account_analytic_id
