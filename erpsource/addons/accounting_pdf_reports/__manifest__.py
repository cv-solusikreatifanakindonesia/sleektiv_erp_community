# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Accounting PDF Reports',
    'version': '2.0.1.0.0',
    'category': 'Invoicing Management',
    'summary': 'Accounting Reports',
    'sequence': '10',
    'author': 'FlectraHQ, Odoo Mates, Odoo SA',
    'license': 'LGPL-3',
    'company': 'FlectraHQ',
    'maintainer': 'FlectraHQ',
    'website': 'https://www.flectrahq.com',
    'depends': ['account'],
    'demo': [],
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'views/account_pdf_reports.xml',
        'views/account_reports_settings.xml',
        'wizards/partner_ledger.xml',
        'wizards/general_ledger.xml',
        'wizards/trial_balance.xml',
        'wizards/balance_sheet.xml',
        'wizards/profit_and_loss.xml',
        'wizards/tax_report.xml',
        'wizards/aged_partner.xml',
        'wizards/journal_audit.xml',
        'reports/report.xml',
        'reports/report_partner_ledger.xml',
        'reports/report_general_ledger.xml',
        'reports/report_trial_balance.xml',
        'reports/report_financial.xml',
        'reports/report_tax.xml',
        'reports/report_aged_partner.xml',
        'reports/report_journal_audit.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'images': ['static/description/banner.gif'],
    'qweb': [],
}
