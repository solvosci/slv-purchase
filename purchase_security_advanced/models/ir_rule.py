# © 2024 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import api, models, tools
from odoo.osv import expression
from odoo.tools import config


class IrRule(models.Model):
    _inherit = "ir.rule"

    @api.model
    @tools.conditional(
        "xml" not in config["dev_mode"],
        tools.ormcache(
            "self.env.uid",
            "self.env.su",
            "model_name",
            "mode",
            "tuple(self._compute_domain_context_values())",
        ),
    )
    def _compute_domain(self, model_name, mode="read"):
        """Inject extra domain for restricting partners when the user
        has the group 'Purchase / User: Own Documents Only'.
        """
        res = super()._compute_domain(model_name, mode=mode)
        user = self.env.user

        # Purchases: 
        P0 = "purchase.group_purchase_user" # Purchases: all documents
        P1 = "purchase_security.group_purchase_own_orders" # Purchases: own documents
        P2 = "purchase.group_purchase_manager" # Purchase Manager

        # Sales:
        S0 = "sales_team.group_sale_salesman" # Sales: own documents
        S1 = "sales_team.group_sale_salesman_all_leads" # Sales: all documents
        S2 = "sales_team.group_sale_manager" # Sales Manager

        if model_name == "res.partner" and not self.env.su:
            if user.has_group(S1) or user.has_group(P2) or (user.has_group(P0) and not user.has_group(P1)):
                pass
            elif user.has_group(S0) or user.has_group(P1):
                if user.has_group(S0) and user.has_group(P1):
                    extra_domain = ['|',
                        ("user_id", "=", user.id),
                        '|',
                        ("purchase_user_id", "=", user.id),
                        ("id", "=", user.partner_id.id),
                    ]
                elif user.has_group(S0):
                    extra_domain = [
                        '|',
                        ("user_id", "=", user.id),
                        ("id", "=", user.partner_id.id),
                    ]
                else:
                    extra_domain = [
                        '|',
                        ("purchase_user_id", "=", user.id),
                        ("id", "=", user.partner_id.id),
                    ]

                extra_domain = expression.normalize_domain(extra_domain)
                res = expression.AND([extra_domain] + [res])
        return res
