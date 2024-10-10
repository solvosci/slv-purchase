# © 2024 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import models, api


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    @api.depends('order_id.picking_type_id')
    def _compute_account_analytic_id(self):
        super()._compute_account_analytic_id()
        for record in self.filtered(lambda x: x.order_id.picking_type_id.warehouse_id.account_analytic_id and not x.display_type):
            record.account_analytic_id = record.order_id.picking_type_id.warehouse_id.account_analytic_id

    @api.depends('order_id.picking_type_id')
    def _compute_analytic_tag_ids(self):
        super()._compute_analytic_tag_ids()
        for record in self.filtered(lambda x: x.order_id.picking_type_id.warehouse_id.account_analytic_tag_ids and not x.display_type):
            record.analytic_tag_ids = record.order_id.picking_type_id.warehouse_id.account_analytic_tag_ids
