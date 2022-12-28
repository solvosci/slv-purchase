# © 2022 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models, fields


class StockProductionLot(models.Model):
    _inherit = "stock.production.lot"

    fcd_document_line_product_qty = fields.Float(related="fcd_document_line_id.product_qty")
    fcd_document_line_price_unit = fields.Float(related="fcd_document_line_id.price_unit")
    currency_id = fields.Many2one(related ='fcd_document_line_id.currency_id')
    fcd_document_line_subtotal = fields.Monetary(related ='fcd_document_line_id.subtotal')
