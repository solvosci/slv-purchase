# © 2023 Solvos Consultoría Informática (<https://www.solvos.es>)
# License AGPL-3 - See https://www.gnu.org/licenses/agpl-3.0.html

from odoo import api, models


class PurchaseOrderLine(models.Model):
    _inherit = "purchase.order.line"

    @api.model_create_multi
    def create(self, vals_list):
        order_ids = self.env["purchase.order"].browse(
            [values.get("order_id") for values in vals_list]
        )
        order_dict = {
            order.id: (
                {
                    order.order_type.analytic_account_id.id: 100,
                }
                if order.order_type.analytic_account_id
                else {}
            )
            for order in order_ids
        }
        # TODO if analytic_distribution is already filled? This overwrites it
        for values in vals_list:
            values["analytic_distribution"] = order_dict.get(values.get("order_id"))
        return super().create(vals_list)
