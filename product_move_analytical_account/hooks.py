# © 2023 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

import logging
from odoo import SUPERUSER_ID, api


def post_init_hook(cr, registry):
    logging.getLogger('odoo.addons.interface_gaia').info(
        'Add Account Analytic from old purchase order line to stock.move.line')

    env = api.Environment(cr, SUPERUSER_ID, {})

    for record in env["stock.move.line"].search([('account_analytic_id', '=', False)]):
        record.account_analytic_id = record.move_id.purchase_line_id.account_analytic_id
