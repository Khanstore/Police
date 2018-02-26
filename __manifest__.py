# -*- coding: utf-8 -*-
{
    'name': "police",

    'summary': """
        This app is designed by SM Ashraf to implement Ribons in eagle ERP""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Eagle IT ",
    'website': "http://www.khan store.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Khan store',
    'version': '0.1',
	'application': 'True',
	'installable' : 'True',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}