# © 2024 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See https://www.gnu.org/licenses/lgpl-3.0.html
from odoo import models
from datetime import timedelta

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    def button_confirm(self):
        super().button_confirm()
        for order in self:
            if order.date_order and order.date_planned:
                dif = (order.date_approve - order.date_order).days
                new_date_planned = order.date_planned + timedelta(days=dif)
                order.write({'date_planned': new_date_planned})
