# -*- coding: utf-8 -*-
# Part of Odoo, Flectra, Sleektiv. See LICENSE file for full copyright and licensing details.

{
    'name': 'Accounting',
    'version': '2.0.1.0.0',
    'category': 'Accounting',
    'summary': 'Accounting Reports, Asset Management and Account Budget For Sleektiv Community Edition',
    'sequence': '1',
    'website': 'https://www.flectrahq.com',
    'author': 'FlectraHQ, Odoo Mates, Odoo SA',
    'company': 'SleektivHQ',
    'maintainer': 'SleektivHQ',
    'license': 'LGPL-3',
    'depends': ['web_sleektiv','accounting_pdf_reports', 'account_asset',
                'account_budget'],
    'demo': [],
    'data': [
        'security/ir.model.access.csv',
        'security/account_security.xml',
        'views/account.xml',
        'views/account_type.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'images': ['static/description/banner.png'],
    'qweb': [],
}
