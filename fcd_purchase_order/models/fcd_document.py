# © 2022 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

from odoo import models, fields, api


class FcdDocument(models.Model):
    _inherit ='fcd.document'

    fao_zone_origin = fields.Char()
