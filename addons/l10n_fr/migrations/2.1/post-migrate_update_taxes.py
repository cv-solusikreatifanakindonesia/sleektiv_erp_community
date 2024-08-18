# Part of Odoo, Flectra, Sleektiv. See LICENSE file for full copyright and licensing details.
from sleektiv.addons.account.models.chart_template import update_taxes_from_templates


def migrate(cr, version):
    update_taxes_from_templates(cr, 'l10n_fr.l10n_fr_pcg_chart_template')
