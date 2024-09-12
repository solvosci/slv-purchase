# © 2023 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

from datetime import datetime
import pdb
from odoo import api, fields, models

class AccountAnalyticAccount(models.Model):
    _inherit = "stock.picking"

    @api.one
    @api.depends('move_lines.date_expected')
    def _compute_scheduled_date(self):
        if self.purchase_id.date_order:
            purchase_date_order = datetime.strptime(self.purchase_id.date_order, "%Y-%m-%d %H:%M:%S")
            purchase_date_planned = datetime.strptime(self.purchase_id.date_planned, "%Y-%m-%d %H:%M:%S")
            deltatime_difference = purchase_date_planned - purchase_date_order
            today_day = datetime.strptime(fields.Datetime.now(), "%Y-%m-%d %H:%M:%S")
            self.scheduled_date = (today_day + deltatime_difference).strftime("%Y-%m-%d %H:%M:%S")
