# -*- coding: utf-8 -*-
{
    'name' : 'Import/Export invoices with Factur-X',
    'version' : '1.0',
    'category': 'Accounting/Accounting',
    'depends' : ['account_edi'],
    'data': [
        'data/account_edi_data.xml',
        'data/facturx_templates.xml',
    ],
    'installable': True,
    'post_init_hook': '_post_init_hook',
    'application': False,
    'auto_install': True,
    'license': 'LGPL-3',
}
