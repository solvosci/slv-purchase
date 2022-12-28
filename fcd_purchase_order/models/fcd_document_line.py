# © 2022 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models, fields, api


class FcdDocumentLine(models.Model):
    _inherit ='fcd.document.line'

    name = fields.Char(compute="_compute_name", store=True)
    purchase_order_line_id = fields.Many2one('purchase.order.line', string='Description')
    product_qty = fields.Float(related ='purchase_order_line_id.product_qty')
    price_unit = fields.Float(related ='purchase_order_line_id.price_unit')
    currency_id = fields.Many2one(related ='purchase_order_line_id.currency_id')
    subtotal = fields.Monetary(related ='purchase_order_line_id.price_subtotal')

    @api.depends('purchase_order_line_id.order_id.name', 'lot_id.name')
    def _compute_name(self):
        for record in self:
            record.name = '%s - %s' % (record.purchase_order_line_id.order_id.name, record.lot_id.name) 
