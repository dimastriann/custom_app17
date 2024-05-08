# -*- coding: utf-8 -*-
{
    "name": "ark_dev_training",
    "summary": "Arkana Technical Training",
    "author": "PT. Arkana Solusi Digital",
    "website": "https://arkana.co.id",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    "category": "Uncategorized",
    "version": "17.0.1.0.0",
    # any module necessary for this one to work correctly
    "depends": ["web", "hr", "report_xlsx", "sale", "mail"],
    # always loaded
    "data": [
        'security/ir.model.access.csv',
        'security/security.xml',
        "report/training_report.xml",
        "report/sale_report_wizard_views.xml",
        "report/training_report_template.xml",
        # "report/sale_order_report_inherit.xml",
        "views/arkana_training_views.xml",
        "views/product_views.xml",
        "views/sale_order_clone_views.xml",
        "views/sale_order_views.xml",
        "views/delegation_views.xml",
        "data/sequence.xml",
        "views/menu_items.xml",
    ],
    # only loaded in demonstration mode
    "demo": [
        # "demo/demo.xml",
    ],

    # "assets": {
    #     "web.assets_backend": [
    #         "/ark_dev_training/static/src/custom_table_odoo.scss",
    #     ]
    # }
    # ,
    "license": "AGPL-3",
}
