# -*- coding: utf-8 -*-
# Part of Odoo, Flectra, Sleektiv. See LICENSE file for full copyright and licensing details.

from sleektiv import api, fields, models, _

class AccountChartTemplate(models.Model):
    _inherit = 'account.chart.template'

    def _load(self, sale_tax_rate, purchase_tax_rate, company):
        rslt = super()._load( sale_tax_rate, purchase_tax_rate, company)

        if company.account_tax_fiscal_country_id in self.env.ref('base.europe').country_ids:
            company._map_eu_taxes()

        return rslt
