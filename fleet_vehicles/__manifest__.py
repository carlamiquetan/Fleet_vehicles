# -*- coding: utf-8 -*-
{
    'name': "fleet_vehicles",

    'summary': """
        Vehicles fleet management
    """,

    'author': "Carla Miquetan",
    'website': "https://www.linkedin.com/in/carla-miquetan/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Operations',
    'version': '0.1',
    'application': True,

    'depends': ['base', 'mail'],

    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'reports/vehicles_template.xml',
        'reports/vehicles_report.xml',
        'wizards/views.xml',
    ],

    'demo': [
        'demo/demo.xml',
    ],
}
