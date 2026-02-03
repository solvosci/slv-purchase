# © 2026 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

from odoo import models

class PurchaseOrderLine(models.Model):
    _inherit = "purchase.order.line"

    def _get_product_purchase_description(self, product_lang):
        self.ensure_one()

        product_lang = product_lang.with_context(
            display_default_code=False
        )

        return super()._get_product_purchase_description(product_lang)
