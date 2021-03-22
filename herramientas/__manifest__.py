# -*- coding: utf-8 -*-
{
    'name': "herramientas",

    'summary': """
        Modulo de herramientas""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Etienne",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail', 'project', 'product'],

    # always loaded
    'data': [
        'views/views.xml',
        'views/herramientasViews.xml',
        'views/horasViews.xml',
        'views/templates.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    'application' : 'True', 
}