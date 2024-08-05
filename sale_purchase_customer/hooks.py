# © 2024 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

import logging

def pre_init_hook(cr):
    logger = logging.getLogger(__name__)
    logger.info(
        "Adding purchase_order.sale_partner_id column if it does not yet exist, "
        "in order to prevent computing every PO"
    )
    cr.execute(
        "ALTER TABLE purchase_order ADD COLUMN IF NOT EXISTS sale_partner_id INTEGER"
    )
