# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import models


class ProductProduct(models.Model):
    _inherit = "product.product"

    def _select_seller(
        self,
        partner_id=False,
        quantity=0.0,
        date=None,
        uom_id=False,
        ordered_by="price_discounted",
        params=False
    ):
        product_obj = self
        if self.env.context.get("skip_sellers_permissions", False):
            product_obj = self.sudo()
        return super(ProductProduct, product_obj)._select_seller(
            partner_id=partner_id,
            quantity=quantity,
            date=date,
            uom_id=uom_id,
            ordered_by=ordered_by,
            params=params
        )
