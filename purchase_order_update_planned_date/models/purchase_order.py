# © 2024 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See https://www.gnu.org/licenses/lgpl-3.0.html
from odoo import models
from datetime import datetime, timedelta

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    def button_approve(self, force=False):
        date_approve = datetime.now()
        for order_line in self.order_line:
            if order_line.order_id.date_order and order_line.date_planned:
                dif = (date_approve - order_line.order_id.date_order).days
                new_date_planned = order_line.date_planned + timedelta(days=dif)
                order_line.write({'date_planned': new_date_planned})
        super().button_approve(force=force)
