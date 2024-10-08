#-*- coding:utf-8 -*-
# Part of Odoo, Flectra, Sleektiv. See LICENSE file for full copyright and licensing details.

# Copyright (C) 2013-2015 Akretion (http://www.akretion.com)

{
    'name': 'France - FEC',
    'category': 'Accounting/Localizations/Reporting',
    'summary': "Fichier d'Échange Informatisé (FEC) for France",
    'author': "Akretion,Sleektiv Community Association (OCA)",
    'depends': ['l10n_fr', 'account'],
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'wizard/account_fr_fec_view.xml',
    ],
    'auto_install': True,
    'license': 'LGPL-3',
}
