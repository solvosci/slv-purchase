# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html
from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    group_taxes_on_report_purchaseorder_document = fields.Boolean(
        string="Display Taxes on Purchase Order Reports",
        implied_group="purchase_order_report_wo_taxation.group_taxes_on_report_purchaseorder_document",
    )
