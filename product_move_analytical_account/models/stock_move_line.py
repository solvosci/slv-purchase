# © 2023 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

from odoo import api, fields, models


class AccountAnalyticAccount(models.Model):
    _inherit = "stock.move.line"

    account_analytic_id = fields.Many2one('account.analytic.account',
        string="Account Analytic",
        compute="_compute_account_analytic",
        store=True)

    @api.multi
    @api.depends('move_id.purchase_line_id.account_analytic_id')
    def _compute_account_analytic(self):
        for record in self:
            record.account_analytic_id = record.move_id.purchase_line_id.account_analytic_id
