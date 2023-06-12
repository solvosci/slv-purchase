# © 2023 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3.0 (https://www.gnu.org/licenses/agpl-3.0.html)
from openupgradelib import openupgrade


@openupgrade.migrate()
def migrate(env, version):
    openupgrade.logged_query(
        env.cr,
        """
        update
            stock_move
        set
            po_menu_invoice_first_date=smmin.mindate
        from (
            select
                sm.id, min(aml.date) mindate
            from
                stock_move sm
            inner join
                stock_move_invoice_line_rel smilr
                on smilr.move_id = sm.id
            inner join
                account_move_line aml
                on aml.id = smilr.invoice_line_id
            where
                sm.purchase_line_id is not null
                and sm.state = 'done'
            group by
                sm.id
        ) as smmin
        where
            stock_move.id=smmin.id
        """,
    )
