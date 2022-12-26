# © 2022 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html
{
    "name": "FCD Purchase Order",
    "summary": """
        Adds purchase order link with fcd
    """,
    "author": "Solvos",
    "license": "LGPL-3",
    "version": "14.0.1.0.0",
    "category": "Purchase",
    "website": "https://github.com/solvosci/slv-purchase",
    "depends": [
        "purchase_order_secondary_unit",
        "product_secondary_unit",
        "stock_secondary_unit",
        "crnd_web_widget_scan_qrcode",
        "web_domain_field",
        "fcd",
        "sequence_reset_period",
    ],
    "data": [
        "data/ir_sequence.xml",
        "security/fcd_purchase_order_security.xml",
        "security/ir.model.access.csv",
        "reports/fcd_purchase_order_tag_report.xml",
        "reports/fcd_purchase_order_tag_template.xml",
        "views/purchase_menu.xml",
        "views/purchase_order_views.xml",
        "views/fcd_document_views.xml",
        "views/fcd_document_line_views.xml",
        "views/stock_production_lot_views.xml",
        "wizards/fcd_purchase_order_wizard_views.xml",
    ],
    'installable': True,
}
