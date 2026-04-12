# © 2026 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

from odoo import api, models, fields


class ProductCategory(models.Model):
    _inherit = "product.category"

    property_cm_standard_auto_upd = fields.Boolean(
        string="Standard Price Cost Method - automatic price update",
        help="""
        When Cost Method is set to 'standard price', setting this will
        enable automatic product standar price update when a incoming
        picking that comes from a purchase is validated.
        This let is keeping our products cost always up-to-date the
        last purchase
        """,
        default=False,
        compute="_compute_property_cm_standard_auto_upd",
        store=True,
        readonly=False,
        company_dependent=True,
    )

    @api.depends("property_cost_method")
    def _compute_property_cm_standard_auto_upd(self):
        self.filtered(
            lambda x: x.property_cost_method != "standard"
        ).property_cm_standard_auto_upd = False
