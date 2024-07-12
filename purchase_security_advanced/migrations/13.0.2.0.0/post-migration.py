# © 2024 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from openupgradelib import openupgrade


@openupgrade.migrate()
def migrate(env, version):
    openupgrade.logged_query(
        env.cr,
        """
        UPDATE
            res_partner
        SET
            purchase_user_id = user_id
        WHERE
            active = true
            AND user_id IS NOT NULL
        """,
    )
