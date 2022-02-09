# © 2022 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

from odoo import api, fields, models


class PurchaseOrderLine(models.Model):
    _inherit = "purchase.order.line"

    product_low_code = fields.Char(
        compute="_compute_product_low_code",
        string="Low Code",
        help="Custom Low Code for this order line."
        "This is initially filled with product LoW Code",
        store=True,
        readonly=False,
    )

    @api.depends("product_id")
    def _compute_product_low_code(self):
        for line in self:
            line.product_low_code = line.product_id.low_code
