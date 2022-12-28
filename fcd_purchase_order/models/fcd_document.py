# © 2022 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models, fields, api


class FcdDocument(models.Model):
    _inherit ='fcd.document'

    fao_zone_origin = fields.Char()
