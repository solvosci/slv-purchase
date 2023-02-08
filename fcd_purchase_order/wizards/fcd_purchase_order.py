# © 2022 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models, fields, _, api
from odoo.exceptions import ValidationError
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
    qr_code2 = fields.Text(string="Insert QR Code")
    lot = fields.Char()
    sanity_reg = fields.Char()
    tide_start_date = fields.Date()
    tide_end_date = fields.Date()
    packaging_date = fields.Date(default=fields.Date.today())
    expiration_date = fields.Date()
    fao_zone = fields.Char()
    fao = fields.Char()
    specific_lot = fields.Char()
    scientific_name = fields.Char()
    net_weight = fields.Float()
    packing = fields.Char()

    commercial_name = fields.Char()
    ship = fields.Char()
    ship_license_plate = fields.Char()
    production_method = fields.Char()
    fishing_gear = fields.Char()
    presentation = fields.Char()

    qr_type = fields.Char()

    total_weight = fields.Boolean()

    ship_id = fields.Many2one('fcd.ship')
    ship_license_plate_rel = fields.Char(related="ship_id.license_plate")
    production_method_id = fields.Many2one('fcd.production.method')
    fishing_gear_id = fields.Many2one('fcd.fishing.gear')
    presentation_id = fields.Many2one('fcd.presentation')
    subzone_id = fields.Many2one('fcd.fao.subzone')


    @api.onchange('ship_id')
    def _onchange_ship_id(self):
        for record in self:
            record.ship = record.ship_id.name

    @api.onchange('ship_license_plate_rel')
    def _onchange_ship_license_plate_rel(self):
        for record in self:
            record.ship_license_plate = record.ship_license_plate_rel

    @api.onchange('production_method_id')
    def _onchange_production_method_id(self):
        for record in self:
            record.production_method = record.production_method_id.name

    @api.onchange('fishing_gear_id')
    def _onchange_fishing_gear_id(self):
        for record in self:
            record.fishing_gear = record.fishing_gear_id.name

    @api.onchange('presentation_id')
    def _onchange_presentation_id(self):
        for record in self:
            record.presentation = record.presentation_id.name

    @api.onchange('subzone_id')
    def _onchange_subzone_id(self):
        for record in self:
            record.fao_zone = record.subzone_id.name

    @api.depends('commercial_name')
    def _compute_product_id_domain(self):
        for record in self:
            if record.commercial_name and len(self.env['product.product'].search([('name', '=', record.commercial_name)])):
                record.product_id_domain = json.dumps(
                    [('name', '=', record.commercial_name)]
                )
            else:
                record.product_id_domain = json.dumps(
                    [('name', '!=', False)]
                )

    @api.onchange('qr_code2')
    def _onchange_qr_code2(self):
        for record in self:
            if record.qr_code2:
                record.qr_code = record.qr_code2
                record._onchange_qr_code()

    @api.onchange('qr_code')
    def _onchange_qr_code(self):
        for record in self:
            record.qr_code2 = record.qr_code
            if record.qr_code:
                try:
                    if record.qr_code[0] == '{':
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
                        record.tide_start_date = fields.Date.to_date(datetime.datetime.strptime(json_data["FechaInicioMarea"], '%d/%m/%Y'))
                        record.tide_end_date = fields.Date.to_date(datetime.datetime.strptime(json_data["FechaFinMarea"], '%d/%m/%Y'))
                        record.packaging_date = fields.Date.to_date(datetime.datetime.strptime(json_data["FechaEnvasado"], '%d/%m/%Y'))
                        record.expiration_date = fields.Date.to_date(datetime.datetime.strptime(json_data["FechaCaducidad"], '%d/%m/%Y'))
                        record.fao_zone = json_data["ZonaFAO"]
                        record.specific_lot = json_data["LoteEspecifico"]
                        record.net_weight = float(json_data["Neto"].replace(',', '.'))
                        record.packing = json_data["Envasado"]
                        record.scientific_name = False
                        record.ship = json_data["UnidadProductiva"]
                        record.production_method = 'Capturado'
                        record.commercial_name = False
                        record.ship_license_plate = False
                    elif len(record.qr_code.split("|")) > 15:
                        # 0 Lote:17012316254051412052
                        # 1 Barco:SIEMPRE SAN PRUDENCIO
                        # 2 Matricula:FE-2 4-96
                        # 3 Lista:3
                        # 4 FAO:HKE
                        # 5 Fecha:17/01/2023
                        # 6 Peso:19.5 Kg.
                        # 7 Proveedor:PASTOR NAUTA, C.B.
                        # 8 Direcccion:SAN ROMAN DE VILLAESTROFE, 6
                        # 9 Postal:27889
                        # 10 Muncipio:CERVO
                        # 11 Comercial:MERLUZA
                        # 12 Cientifico:MERLUCCIUS MERLUCCIUS
                        # 13 Metodo:CAPTURADO
                        # 14 Zona:27-ATLANTICO NE VIIId Centro de Vizcaya
                        # 15 Arte:Sedales y ANZUELOS
                        # 16 Presentacion:Fresco EVS GUT
                        # 17 Calibre:2
                        # 18 Precio:6.65
                        # 19 N envases:1
                        # 20 Tipo envase:58
                        # 21 Fecha inicio marea:10/01/2023
                        # 22 Fecha fin marea:14/01/2023

                        record.qr_type = 'Burela2'
                        record.qr_code = record.qr_code.replace(" | ", "|")
                        data = record.qr_code.split("|")

                        record.lot = data[0].split(":")[1]
                        record.tide_start_date = fields.Date.to_date(datetime.datetime.strptime(data[21].split(":")[1].strip(), '%d/%m/%Y'))
                        record.tide_end_date = fields.Date.to_date(datetime.datetime.strptime(data[22].split(":")[1].strip(), '%d/%m/%Y'))
                        record.fao_zone = data[14].split(":")[1]
                        record.net_weight = float(data[6].split(":")[1].split("K")[0])
                        record.scientific_name = data[12].split(":")[1]
                        record.price = float(record.qr_code.split("|")[18].split(":")[1])

                        record.ship = data[1].split(":")[1]
                        record.ship_license_plate = data[2].split(":")[1]
                        record.fishing_gear = data[15].split(":")[1]
                        record.production_method = data[13].split(":")[1].lower().capitalize().strip()
                        record.presentation = data[16].split(":")[1]
                        record.commercial_name = data[11].split(":")[1]

                        record.packaging_date = False
                        record.expiration_date = False
                        record.packing = False
                        record.specific_lot = False
                        record.sanity_reg = False
                    elif record.qr_code[0] != '{':
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

                        record.packaging_date = False
                        record.expiration_date = False
                        record.fao_zone = data[13]

                        record.tide_start_date = fields.Date.to_date(datetime.datetime.strptime(data[15], '%d/%m/%Y'))
                        record.tide_end_date = fields.Date.to_date(datetime.datetime.strptime(data[16], '%d/%m/%Y'))

                        record.specific_lot = False
                        record.net_weight = data[17]
                        record.packing = False

                        record.ship = data[3]
                        record.ship_license_plate = data[4]
                        record.fishing_gear = data[14]
                        record.production_method = data[12]
                        record.presentation = data[9]
                        record.commercial_name = data[5]
                except Exception as Ex:
                    raise ValidationError(
                        _("Invalid QR Code!")
                    )
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
                record.partner_id = self.env['res.partner'].search(['|', ('name', 'like', data[1]), ('second_name_fcd', 'like', data[1])], limit=1)
                record.product_id = self.env['product.product'].search([('name', '=', record.commercial_name)], limit=1)
            elif record.qr_type == 'Burela':
                pass
            elif record.qr_type == 'Burela2':
                record.qr_code = record.qr_code.replace(" |", "|")
                data = record.qr_code.split("|")
                record.partner_id = self.env['res.partner'].search(['|', ('name', 'like', data[7].split(":")[1]), ('second_name_fcd', 'like', data[7].split(":")[1])], limit=1)
                record.product_id = self.env['product.product'].search([('name', '=', data[12].split(":")[1])], limit=1)

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
        if not fcd_document_id:
            fcd_document_id = fcd_document_id.sudo().create({
                'name': lot_name,
                'partner_id': self.partner_id.id,
                'product_id': self.product_id.id,
                'tide_start_date': self.tide_start_date,
                'tide_end_date': self.tide_end_date,
                'packaging_date': self.packaging_date,
                'expiration_date': self.expiration_date,
                'fao_zone': self.fao_zone,
                'specific_lot': self.specific_lot,
                'packing': self.packing,
                'ship': self.ship,
                'ship_license_plate': self.ship_license_plate,
                'production_method': self.production_method,
                'fishing_gear': self.fishing_gear,
                'presentation': self.presentation
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
            if self.total_weight:
                quantity = self.net_weight
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
        self.qr_code = False
        self.qr_code2 = False
        self.lot = False
        self.sanity_reg = False
        self.tide_start_date = False
        self.tide_end_date = False
        self.packaging_date = False
        self.expiration_date = False
        self.fao_zone = False
        self.specific_lot = False
        self.scientific_name = False
        self.net_weight = False
        self.packing = False
        self.qr_type = False
        self.ship = False
        self.ship_license_plate = False
        self.production_method = False
        self.fishing_gear = False
        self.presentation = False
        self.commercial_name = False
        return self.env['purchase.order']._purchase_qr_code_reading_open_wizard(self.id)

    def save_and_next_purchase_order_line(self):
        self.create_update_purchase_order_line()
        self.qr_code = False
        self.qr_code2 = False
        return self.env['purchase.order']._purchase_qr_code_reading_open_wizard(self.id)

    def save_and_close_purchase_order_line(self):
        self.create_update_purchase_order_line()
        return {
            'type': 'ir.actions.client',
            'tag': 'reload',
        }
