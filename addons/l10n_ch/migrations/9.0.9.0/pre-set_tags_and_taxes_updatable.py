# -*- coding: utf-8 -*-

import sleektiv

def migrate(cr, version):
    registry = sleektiv.registry(cr.dbname)
    from sleektiv.addons.account.models.chart_template import migrate_set_tags_and_taxes_updatable
    migrate_set_tags_and_taxes_updatable(cr, registry, 'l10n_ch')

