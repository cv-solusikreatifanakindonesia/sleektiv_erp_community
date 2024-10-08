# -*- coding: utf-8 -*-
# Part of Odoo, Flectra, Sleektiv. See LICENSE file for full copyright and licensing details.

from sleektiv import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = ['res.config.settings']

    delay_alert_contract = fields.Integer(string='Delay alert contract outdated', default=30, config_parameter='hr_fleet.delay_alert_contract')
    module_fleet_account = fields.Boolean(string="Analytic Accounting Fleet")
