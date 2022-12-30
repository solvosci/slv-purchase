# © 2023 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

from odoo import _, models
from odoo.tools.float_utils import float_compare


class PurchaseOrderLine(models.Model):
    _inherit = "purchase.order.line"

    def _create_or_update_picking(self):
        # Lines that will raise an error that we want to prevent
        decreased_lines = self.filtered(
            lambda x: 
            x.product_id
            and x.product_id.type in ["product", "consu"]
            and float_compare(
                x.product_qty,
                x.qty_received,
                precision_rounding=x.product_uom.rounding
            ) < 0
        )
        for line in decreased_lines:
            # Ignoring super() call this control should be omitted, so we copy
            #  it again.
            # Source: https://github.com/odoo/odoo/blob/14.0/addons/purchase_stock/models/purchase.py#L367
            if float_compare(line.product_qty, line.qty_invoiced, precision_rounding=line.product_uom.rounding) == -1:
                line.invoice_lines[0].move_id.activity_schedule(
                    'mail.mail_activity_data_warning',
                    note=_('The quantities on your purchase order indicate less than billed. You should ask for a refund.')
                )
            
        # For the other lines, operation should work as expected
        super(
            PurchaseOrderLine,
            self - decreased_lines
        )._create_or_update_picking()
