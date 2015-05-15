# -*- coding: utf-8 -*-
{
    'name': "l10n_co_base_partner",

    'summary': """
        l10n_co_base_partner""",

    'description': """
        l10n_co_base_partner
    """,

    'author': "FONSE SAS",
    'website': "http://www.fonse.net",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Extra Tools',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'res_users_view.xml',
        'res_partner_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [ 
    ],
    'installable': True,
    'auto_install': False,    
}
