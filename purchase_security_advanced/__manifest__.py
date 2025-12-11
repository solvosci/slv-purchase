# © 2021 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
{
    "name": "Purchase Security - Advanced",
    "summary": """
        Adds extra security for Purchase Order security schema
    """,
    "author": "Solvos",
    "license": "AGPL-3",
    "version": "17.0.1.0.2",
    'category': "Operations/Purchase",
    "website": "https://github.com/solvosci/slv-purchase",
    "depends": ["purchase_security"],
    "excludes": ["sales_team_security"],
    "data": [
        "views/res_partner_views.xml",
    ],
    'installable': True,
}
