# © 2022 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

from odoo import models, fields, _


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    fcd_document_line_id = fields.Many2one('fcd.document.line')
    fcd_lot_name = fields.Char()
    fcd_lot_id = fields.Many2one('stock.production.lot', related="fcd_document_line_id.lot_id")
    fcd_lot_finished = fields.Boolean()
