# © 2023 Solvos Consultoría Informática (<https://www.solvos.es>)
# License AGPL-3 - See https://www.gnu.org/licenses/agpl-3.0.html

from odoo import api, models


class PurchaseOrderLine(models.Model):
    _inherit = "purchase.order.line"

    @api.model
    def create(self, values):
        order_id = self.env["purchase.order"].browse(
            values.get("order_id")
        )
        if order_id.order_type.analytic_account_id:
            values["account_analytic_id"] = order_id.order_type.analytic_account_id.id
        return super().create(values)
