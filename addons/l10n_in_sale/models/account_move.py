# -*- coding: utf-8 -*-
# Part of Odoo, Flectra, Sleektiv. See LICENSE file for full copyright and licensing details.

from sleektiv import api, models


class AccountMove(models.Model):
    _inherit = "account.move"

    def _l10n_in_get_shipping_partner(self):
        shipping_partner = super()._l10n_in_get_shipping_partner()
        return self.partner_shipping_id or shipping_partner

    @api.model
    def _l10n_in_get_shipping_partner_gstin(self, shipping_partner):
        return shipping_partner.l10n_in_shipping_gstin
