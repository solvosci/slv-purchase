# © 2022 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

from odoo import models, fields, _, api
import re
import json
import datetime


class FCDPurchaseOrder(models.TransientModel):
    _name = 'fcd.purchase.order.wizard'
    _description = 'fcd.purchase.order.wizard'

    partner_id = fields.Many2one('res.partner')
    product_id = fields.Many2one('product.product')
    tag_number = fields.Integer(default=1)
    price = fields.Float()

    product_id_domain = fields.Char(
        compute="_compute_product_id_domain",
        readonly=True,
        store=False,
    )

    purchase_order_id = fields.Many2one('purchase.order',)
    editable_lot = fields.Char()
    quantity = fields.Float()

    qr_code = fields.Char()
    lot = fields.Char(compute="_compute_qr_code_data")
    sanity_reg = fields.Char(compute="_compute_qr_code_data")
    ship_name = fields.Char(compute="_compute_qr_code_data")
    tide_start_date = fields.Date(compute="_compute_qr_code_data")
    tide_end_date = fields.Date(compute="_compute_qr_code_data")
    packaging_date = fields.Date(compute="_compute_qr_code_data")
    expiration_date = fields.Date(compute="_compute_qr_code_data")
    fao_zone = fields.Char(compute="_compute_qr_code_data")
    fao = fields.Char(compute="_compute_qr_code_data")
    specific_lot = fields.Char(compute="_compute_qr_code_data")
    scientific_name = fields.Char()
    net_weight = fields.Float(compute="_compute_qr_code_data")
    packing = fields.Char(compute="_compute_qr_code_data")

    ship_id = fields.Many2one('fcd.ship')
    production_method_id = fields.Many2one('fcd.production.method')
    fishing_gear_id = fields.Many2one('fcd.fishing.gear')
    country_id = fields.Many2one('res.country')
    presentation_id = fields.Many2one('fcd.presentation')

    qr_type = fields.Char(compute="_compute_qr_code_data")

    @api.depends('scientific_name')
    def _compute_product_id_domain(self):
        for record in self:
            if record.scientific_name:
                record.product_id_domain = json.dumps(
                    [('scientific_name', 'like', record.scientific_name)]
                )
            else:
                record.product_id_domain = json.dumps(
                    [('name', '!=', False)]
                )

    @api.onchange('qr_code')
    def _onchange_qr_code(self):
        for record in self:
            if record.qr_type == 'Coruña':
                record.qr_code = record.qr_code.replace("\n", " ")

                pattern = r'(?<= )[a-zA-Z()/\.]*:'
                data = re.split(pattern, record.qr_code)
                data.pop(0)

                # Por el momento para quitar los espacios vacios a la derecha
                cont = 0
                for x in data:
                    data[cont] = x.rstrip()
                    cont += 1
                record.scientific_name = data[6]
                record.partner_id = self.env['res.partner'].search([('name', 'like', data[1]), ('second_name_fcd', 'like', data[1])], limit=1)
                record.product_id = self.env['product.product'].search([('scientific_name', 'like', record.scientific_name)], limit=1)
                record.ship_id = self.env['fcd.ship'].search([('license_plate', 'like', data[4])], limit=1)
                record.fishing_gear_id = self.env['fcd.fishing.gear'].search([('name', 'like', data[14])], limit=1)

                record.fishing_gear_id = self.env['fcd.fishing.gear'].search([('name', 'like', data[14])], limit=1)
                record.production_method_id = self.env['fcd.production.method'].search([('name', 'like', data[12])])

                record.presentation_id = self.env['fcd.presentation'].search([('code', 'like', data[9])], limit=1)
                if not record.presentation_id:
                    record.presentation_id = record.product_id.presentation_id
            elif record.qr_type == 'Burela':
                json_data = json.loads(record.qr_code)
                record.ship_id = self.env['fcd.ship'].search([('name', 'like', json_data["UnidadProductiva"])], limit=1)
                record.production_method_id = self.env.ref('fcd.fcd_production_method_captured')

                if record.ship_id.fishing_gear_ids:
                    record.fishing_gear_id = record.ship_id.fishing_gear_ids[0]
                if not record.ship_id:
                    record.ship_id = self.env.ref("fcd.fcd_ship_1")
                record.presentation_id = record.product_id.fcd_presentation_id

    @api.depends('qr_code')
    def _compute_qr_code_data(self):
        for record in self:
            if record.qr_code:
                if record.qr_code[0] != '{':
                    # ------- Etiquetas Coruña ------------ 
                    #  0 Lote:3009202273CPR 
                    #  1 Comp:SONIA VENTAS S.L. 
                    #  2 R.S:12-18510/C 
                    #  3 Barco:O MARUSIA 
                    #  4 MAT:3 CO-7 2-06 
                    #  5 Com:CAMARON 
                    #  6 Cien:PALAEMON SERRATUS 
                    #  7 Aut:CAMARON COMUN 
                    #  8 FAO:CPR 
                    #  9 Pres:WHL 
                    # 10 Cal:1 
                    # 11 Fresc:E 
                    # 12 M.Prod:Capturado
                    # 13 Z.Cap:FAO-27.9.A
                    # 14 A.Pesca:Nasas
                    # 15 Ini:29/09/2022
                    # 16 Fin:30/09/2022
                    # 17 Peso:3.50
                    # 18 T.(Kg):1.50
                    # 19 P.M.P:0.00
                    record.qr_type = 'Coruña'
                    record.qr_code = record.qr_code.replace("\n", " ")

                    pattern = r'(?<= )[a-zA-Z()/\.]*:'
                    data = re.split(pattern, record.qr_code)
                    data.pop(0)

                    # Por el momento para quitar los espacios vacios a la derecha
                    cont = 0
                    for x in data:
                        data[cont] = x.rstrip()
                        cont += 1

                    record.lot = data[0]
                    record.sanity_reg = data[2]
                    record.ship_name = data[3]
                    record.fao = data[8]

                    record.packaging_date = False
                    record.expiration_date = False
                    record.fao_zone = data[13]

                    record.tide_start_date = fields.Date.to_date(datetime.datetime.strptime(data[15], '%d/%m/%Y'))
                    record.tide_end_date = fields.Date.to_date(datetime.datetime.strptime(data[16], '%d/%m/%Y'))

                    record.specific_lot = False
                    record.net_weight = data[17]
                    record.packing = False
                elif record.qr_code[0] == '{':
                    # ------- Etiquetas Burela -------
                    # {
                    #   "Lote":"HKEV1-21306OLG05",
                    #   "RegSanitario":"",
                    #   "UnidadProductiva":"OLGA",
                    #   "FechaInicioMarea":"31/05/2022",
                    #   "FechaFinMarea":"12/06/2022",
                    #   "FechaEnvasado":"13/06/2022",
                    #   "FechaCaducidad":"21/06/2022",
                    #   "ZonaFAO":"27-ATLANTICO NE VIIIA NORDESTE DE VIZCAYA",
                    #   "FAO":"HKE",
                    #   "LoteEspecifico":"2022146000012116",
                    #   "Neto":"0,1",
                    #   "Envasado":"12.10250/LU"
                    # }
                    record.qr_type = 'Burela'
                    json_data = json.loads(record.qr_code)
                    record.lot = json_data["Lote"]
                    record.sanity_reg = json_data["RegSanitario"]
                    record.ship_name = json_data["UnidadProductiva"]
                    record.tide_start_date = fields.Date.to_date(datetime.datetime.strptime(json_data["FechaInicioMarea"], '%d/%m/%Y'))
                    record.tide_end_date = fields.Date.to_date(datetime.datetime.strptime(json_data["FechaFinMarea"], '%d/%m/%Y'))
                    record.packaging_date = fields.Date.to_date(datetime.datetime.strptime(json_data["FechaEnvasado"], '%d/%m/%Y'))
                    record.expiration_date = fields.Date.to_date(datetime.datetime.strptime(json_data["FechaCaducidad"], '%d/%m/%Y'))
                    record.fao_zone = json_data["ZonaFAO"]
                    record.fao = json_data["FAO"]
                    record.specific_lot = json_data["LoteEspecifico"]
                    record.net_weight = float(json_data["Neto"].replace(',', '.'))
                    record.packing = json_data["Envasado"]
                    record.scientific_name = False
            else:
                record.lot = False
                record.sanity_reg = False
                record.ship_name = False
                record.tide_start_date = False
                record.tide_end_date = False
                record.packaging_date = False
                record.expiration_date = False
                record.fao_zone = False
                record.fao = False
                record.specific_lot = False
                record.scientific_name = False
                record.net_weight = False
                record.packing = False
                record.qr_type = False

    def create_fcd_document_line(self):
        if self.editable_lot:
            lot_name = self.editable_lot
            self.partner_id = self.purchase_order_id.partner_id
        else:
            lot_name = self.lot
        fcd_document_id = self.env['fcd.document'].search([
            ('name', '=', lot_name),
            ('product_id', '=', self.product_id.id),
            ('partner_id', '=', self.partner_id.id),
        ])
        if self.fao_zone:
            if self.qr_type == 'Burela':
                fao_zone = self.env['fcd.fao.zone'].search([('code', '=', self.fao_zone[0:2])])
                fao_zone_id = self.env['fcd.fao.zone'].search([('code', '=', self.fao_zone[0:2])]).id
                subzone_id = False
                if len(fao_zone.subzone_ids) == 1:
                    subzone_id = fao_zone.subzone_ids.id
            elif self.qr_type == 'Coruña':
                fao_zone = self.env['fcd.fao.zone'].search([('code', '=', self.fao_zone[4:6])])
                fao_zone_id = fao_zone.id
                # subzone_id = self.env['fcd.fao.subzone'].search([('subzone', '=', self.fao_zone[9])]).id
                subzone_id = False
        else:
            fao_zone_id = False
            subzone_id = False
        if not fcd_document_id:
            fcd_document_id = fcd_document_id.sudo().create({
                'name': lot_name,
                'partner_id': self.partner_id.id,
                'product_id': self.product_id.id,
                'sanity_reg': self.sanity_reg,
                'tide_start_date': self.tide_start_date,
                'tide_end_date': self.tide_end_date,
                'packaging_date': self.packaging_date,
                'expiration_date': self.expiration_date,
                'fao_zone_origin': self.fao_zone,
                'fao_zone_id': fao_zone_id,
                'subzone_id': subzone_id,
                'fao': self.fao,
                'specific_lot': self.specific_lot,
                'packing': self.packing,
                'ship_id': self.ship_id.id,
                'production_method_id': self.production_method_id.id,
                'fishing_gear_id': self.fishing_gear_id.id,
            })
        fcd_document_line_id = fcd_document_id.fcd_document_line_ids.filtered(lambda x: x.price_unit == self.price)
        if not fcd_document_line_id:
            fcd_document_line_id = fcd_document_line_id.sudo().create({
                'price_unit': self.price,
                'fcd_document_id': fcd_document_id.id,
            })

        fcd_document_line_id.sudo().write({
            'box_count': fcd_document_line_id.box_count + self.tag_number,
        })
        return fcd_document_line_id

    def create_update_purchase_order_line(self):
        fcd_document_line_id = self.create_fcd_document_line()
        date_start_order = fields.Datetime.to_datetime(fields.Date.today()).strftime("%Y-%m-%d 00:00:00")
        date_end_order = fields.Datetime.to_datetime(fields.Date.today()).strftime("%Y-%m-%d 23:59:59")
        if self.purchase_order_id:
            purchase_order_id = self.purchase_order_id
            quantity = self.quantity
        else:
            purchase_order_id = self.env['purchase.order'].search([
                ('partner_id', '=', self.partner_id.id),
                ('state', '!=', 'cancel'),
                ('date_order','>=', date_start_order),
                ('date_order','<=', date_end_order)], order='id')
            quantity = self.net_weight * self.tag_number
        if not purchase_order_id:
            purchase_order_id = self.env['purchase.order'].create({
                'partner_id': self.partner_id.id
            })
            purchase_order_id[-1].button_confirm()
        line_id = purchase_order_id[-1].order_line.filtered(lambda x: x.fcd_document_line_id == fcd_document_line_id and x.product_id.id == self.product_id.id and x.price_unit == self.price)
        if line_id:
            line_id.write({
                'product_qty': line_id.product_qty + (quantity),
                'secondary_uom_qty': line_id.secondary_uom_qty + (self.tag_number)
            })
        else:
            line_id = line_id.create({
                'order_id': purchase_order_id[-1].id,
                'name': self.product_id.display_name,
                'product_id': self.product_id.id,
                'fcd_document_line_id': fcd_document_line_id.id,
                'product_qty': float(quantity),
                'secondary_uom_qty': self.tag_number,
                'secondary_uom_id': self.product_id.purchase_secondary_uom_id.id,
                'price_unit': self.price,
            })
        lot_id = self.env['stock.production.lot'].sudo().create({
            'name': self.env['ir.sequence'].next_by_code('lot_cigurria'),
            'product_id': self.product_id.id,
            'company_id': self.env.user.company_id.id,
            # 'expiration_date': self.expiration_date, Posibles errores en la báscula en el caso de que se genere una orden de fabricacion en estado pendiente si está caducado, el primer caso no da problemas pero los posteriores si
        })
        fcd_document_line_id.sudo().write({
            'purchase_order_line_id': line_id.id,
            'lot_id': lot_id.id
        })
        lot_id.fcd_document_line_id = fcd_document_line_id.id
        self.tag_number = 1
        self.qr_code = False

    def save_and_new_purchase_order_line(self):
        self.create_update_purchase_order_line()
        self.partner_id = False
        self.product_id = False
        self.price = 0
        return self.env['purchase.order']._purchase_qr_code_reading_open_wizard(self.id)

    def save_and_next_purchase_order_line(self):
        self.create_update_purchase_order_line()
        return self.env['purchase.order']._purchase_qr_code_reading_open_wizard(self.id)

    def save_and_close_purchase_order_line(self):
        self.create_update_purchase_order_line()
        return {
            'type': 'ir.actions.client',
            'tag': 'reload',
        }
