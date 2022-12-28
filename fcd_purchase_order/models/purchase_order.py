# © 2022 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models, fields, _, api


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    def action_purchase_qr_code_reading(self):
        Wizard = self.env['fcd.purchase.order.wizard']
        new = Wizard.create({
            "qr_code": False,
        })
        return self._purchase_qr_code_reading_open_wizard(new.id)

    def _purchase_qr_code_reading_open_wizard(self, purchase_id):
        return {
            'name': _('QR Code Reading'),
            'res_model': 'fcd.purchase.order.wizard',
            'view_mode': 'form',
            'view_type': 'form',
            'res_id': purchase_id,
            'target': 'new',
            'type': 'ir.actions.act_window',
        }

    def action_purchase_order_add_line(self):
        Wizard = self.env['fcd.purchase.order.wizard']
        new = Wizard.create({
            "purchase_order_id": self.id,
        })
        return self._purchase_order_add_line_open_wizard(new.id)

    def _purchase_order_add_line_open_wizard(self, purchase_id):
        return {
            'name': _('Add purchase order line'),
            'res_model': 'fcd.purchase.order.wizard',
            'view_mode': 'form',
            'view_type': 'form',
            'res_id': purchase_id,
            'view_id': self.env.ref(
                "fcd_purchase_order.view_fcd_purchase_order_reduced_wizard"
            ).id,
            'target': 'new',
            'type': 'ir.actions.act_window',
        }

    @api.constrains('order_line')
    def create_fcd_documents(self):
        for line in self.order_line.filtered(lambda x: x.product_type == 'product' and x.fcd_lot_id.id == False):
            if line.fcd_lot_name:
                line.secondary_uom_id = line.product_id.purchase_secondary_uom_id.id
                lot_id = self.env['stock.production.lot'].sudo().create({
                    'name': line.fcd_lot_name,
                    'product_id': line.product_id.id,
                    'company_id': self.env.user.company_id.id,
                })
            else:
                lot_id = self.env['stock.production.lot'].sudo().create({
                    'name': self.env['ir.sequence'].next_by_code('lot_cigurria'),
                    'product_id': line.product_id.id,
                    'company_id': self.env.user.company_id.id,
                })
            today =  _("WITHOUT LOT PR %s/%s/%s") % (
                fields.Datetime().now().day,
                fields.Datetime().now().month,
                fields.Datetime().now().year
            )
            fcd_document_id = self.env['fcd.document'].search([
                ('name', '=', today),
                ('partner_id', '=', line.partner_id.id),
                ('product_id', '=', line.product_id.id)
            ])
            if not fcd_document_id:
                fcd_document_id = self.env['fcd.document'].sudo().create({
                    'name': today,
                    'partner_id': line.partner_id.id,
                    'product_id': line.product_id.id,
                })

            fcd_document_line_id = self.env['fcd.document.line'].sudo().create({
                'fcd_document_id': fcd_document_id.id,
                'purchase_order_line_id': line.id,
                'lot_id': lot_id.id,
            })
            line.fcd_document_line_id = fcd_document_line_id.id,
            lot_id.fcd_document_line_id = fcd_document_line_id.id
