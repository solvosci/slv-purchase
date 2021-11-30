# © 2021 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

from odoo import fields, models


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    date_order_approve = fields.Datetime(related="date_order")
