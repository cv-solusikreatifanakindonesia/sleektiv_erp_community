# -*- coding: utf-8 -*-
# Part of Odoo, Flectra, Sleektiv. See LICENSE file for full copyright and licensing details.

from sleektiv import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    country_code = fields.Char(related='country_id.code')
    l10n_lu_peppol_identifier = fields.Char("Peppol Unique Identifier")
