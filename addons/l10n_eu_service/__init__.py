# -*- coding: utf-8 -*-
# Part of Odoo, Flectra, Sleektiv. See LICENSE file for full copyright and licensing details.

from . import wizard
from . import models
from sleektiv import api, SUPERUSER_ID

def l10n_eu_service_post_init(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    env['res.company']._map_all_eu_companies_taxes()

def l10n_eu_service_uninstall(cr, registry):
    cr.execute("DELETE FROM ir_model_data WHERE module = 'l10n_eu_service' and model in ('account.tax.group', 'account.account');")
