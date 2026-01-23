# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3.0 (https://www.gnu.org/licenses/lgpl-3.0.html)

import logging

_logger = logging.getLogger(__name__)


def pre_init_hook(env):
    _logger.info(
        "Pre-creating column po_menu_exclude for table stock_move"
    )
    env.cr.execute(
        """
        ALTER TABLE stock_move
        ADD COLUMN IF NOT EXISTS po_menu_exclude Boolean;
        """
    )
