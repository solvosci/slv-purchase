# © 2022 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3.0 (https://www.gnu.org/licenses/lgpl-3.0.html)

from odoo import api, fields, models
from odoo.tools import float_compare


class StockMove(models.Model):
    _inherit = "stock.move"

    po_product_categ_id = fields.Many2one(related="product_id.categ_id")
    po_currency_id = fields.Many2one(related="purchase_line_id.currency_id")
    purchase_order = fields.Many2one(
        related="purchase_line_id.order_id",
        store=True,
    )
    purchase_partner_id = fields.Many2one(
        related="purchase_order.partner_id",
        store=True,
    )
    purchase_user_id = fields.Many2one(
        related="purchase_line_id.order_id.user_id",
    )

    po_menu_price_unit = fields.Float(
        compute="_compute_po_menu_price_amount_total",
        string="Unit Price",
        store=True,
    )
    po_menu_price_amount_total = fields.Monetary(
        compute="_compute_po_menu_price_amount_total",
        string="Amount Total",
        currency_field="po_currency_id",
        store=True,
    )
    po_menu_invoice_lines_count = fields.Integer(
        compute="_compute_po_menu_price_amount_total",
        store=True,
    )

    @api.depends(
        "purchase_line_id.price_unit",
        "quantity_done",
        "purchase_line_id.invoice_lines",
        "purchase_line_id.invoice_lines.price_unit",
        "purchase_line_id.invoice_lines.quantity"
    )
    def _compute_po_menu_price_amount_total(self):
        precision = self.env["decimal.precision"].precision_get(
            "Product Price"
        )
        for record in self:
            record.po_menu_invoice_lines_count = len(record.purchase_line_id.invoice_lines)
            prices = [invoice.price_unit for invoice in record.purchase_line_id.invoice_lines]

            if any(1 if float_compare(prices[0], price, precision_digits=precision) else 0 for price in prices) or record.po_menu_invoice_lines_count == 0:
                record.po_menu_price_unit = record.purchase_line_id.price_unit
                record.po_menu_price_amount_total = record.po_menu_price_unit * record.quantity_done
            else:
                record.po_menu_price_unit = prices[0]
                record.po_menu_price_amount_total = record.po_menu_price_unit * record.quantity_done
