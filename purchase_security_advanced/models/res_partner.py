# © 2024 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    user_id = fields.Many2one(index=True)

    purchase_user_id = fields.Many2one(
        comodel_name="res.users",
        string="Purchase Representative",
        index=True
    )
