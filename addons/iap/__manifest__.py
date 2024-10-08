# -*- coding: utf-8 -*-
# Part of Odoo, Flectra, Sleektiv. See LICENSE file for full copyright and licensing details.

{
    'name': 'In-App Purchases',
    'category': 'Hidden/Tools',
    'version': '1.1',
    'summary': 'Basic models and helpers to support In-App purchases.',
    'description': """
This module provides standard tools (account model, context manager and helpers)
to support In-App purchases inside Sleektiv. """,
    'depends': [
        'web',
        'base_setup'
    ],
    'data': [
        'security/ir.model.access.csv',
        'security/ir_rule.xml',
        'views/assets.xml',
        'views/iap_views.xml',
        'views/res_config_settings.xml',
    ],
    'qweb': [
        'static/src/xml/iap_templates.xml',
    ],
    'auto_install': True,
    'license': 'LGPL-3',
}
