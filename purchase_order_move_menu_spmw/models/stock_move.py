# © 2022 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3.0 (https://www.gnu.org/licenses/lgpl-3.0.html)

from odoo import fields, models


class StockMove(models.Model):
    _inherit = "stock.move"

    related_real_po_order_id = fields.Many2one(
        related="purchase_line_id.related_real_order_id",
        string="Related Order",
    )
