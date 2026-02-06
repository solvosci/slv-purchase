# © 2021 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

from odoo import models


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    def _notify_get_reply_to(self, default=None):
        res = super()._notify_get_reply_to(default=default)
        forced = self.env['ir.config_parameter'].sudo().get_param('purchase.reply_to_email')
        if not forced:
            return res
        for po in self:
            res[po.id] = self._notify_get_reply_to_formatted_email(
                forced,
                po.display_name or '',
                company=po.company_id
            )
        return res
