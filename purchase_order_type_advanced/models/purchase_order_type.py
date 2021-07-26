# © 2021 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

from odoo import fields, models


class PurchaseOrderType(models.Model):
    _inherit = "purchase.order.type"

    journal_id = fields.Many2one(
        comodel_name="account.journal",
        string="Billing Journal",
        domain=[("type", "=", "purchase")],
    )
    picking_type_id = fields.Many2one(
        comodel_name='stock.picking.type',
        string='Deliver To'
    )
    pricelist_id = fields.Many2one(
        comodel_name="product.pricelist",
        strint="Pricelist"
    )
