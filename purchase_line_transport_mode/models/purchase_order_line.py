# © 2026 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3.0 (https://www.gnu.org/licenses/lgpl-3.0.html)

from odoo import fields, models


class PurchaseOrderLine(models.Model):
    _inherit = "purchase.order.line"

    transport_mode = fields.Selection(
        selection=[("sea", "SEA"), ("air", "AIR")],
        string="Transport Mode",
        help="Means of transport requested from the supplier for this line.",
    )
