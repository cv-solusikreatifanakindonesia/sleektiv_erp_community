# -*- coding: utf-8 -*-
# Part of Odoo, Flectra, Sleektiv. See LICENSE file for full copyright and licensing details.

from sleektiv import api, fields, models, _
from sleektiv.addons.base_iban.models.res_partner_bank import normalize_iban, pretty_iban, validate_iban
from sleektiv.addons.base.models.res_bank import sanitize_account_number
from sleektiv.exceptions import ValidationError

class ResPartnerBank(models.Model):
    _inherit = 'res.partner.bank'

    l10n_ch_qr_iban = fields.Char(string='QR-IBAN', help="Put the QR-IBAN here for your own bank accounts.  That way, you can "
                                                         "still use the main IBAN in the Account Number while you will see the "
                                                         "QR-IBAN for the barcode.  ")

    def _validate_qr_iban(self, qr_iban):
        # Check first if it's a valid IBAN.
        validate_iban(qr_iban)
        # We sanitize first so that _check_qr_iban_range() can extract correct IID from IBAN to validate it.
        sanitized_qr_iban = sanitize_account_number(qr_iban)
        # Now, check if it's valid QR-IBAN (based on its IID).
        if not self._check_qr_iban_range(sanitized_qr_iban):
            raise ValidationError(_("QR-IBAN '%s' is invalid.") % qr_iban)
        return True

    @api.model
    def create(self, vals):
        if vals.get('l10n_ch_qr_iban'):
            self._validate_qr_iban(vals['l10n_ch_qr_iban'])
            vals['l10n_ch_qr_iban'] = pretty_iban(normalize_iban(vals['l10n_ch_qr_iban']))
        return super().create(vals)

    def write(self, vals):
        if vals.get('l10n_ch_qr_iban'):
            self._validate_qr_iban(vals['l10n_ch_qr_iban'])
            vals['l10n_ch_qr_iban'] = pretty_iban(normalize_iban(vals['l10n_ch_qr_iban']))
        return super().write(vals)

    def _is_qr_iban(self):
        return super(ResPartnerBank, self)._is_qr_iban() or self.l10n_ch_qr_iban

    def _l10n_ch_get_qr_vals(self, amount, currency, debtor_partner, free_communication, structured_communication):
        qr_vals = super()._l10n_ch_get_qr_vals(amount, currency, debtor_partner, free_communication, structured_communication)
        # If there is a QR IBAN we use it for the barcode instead of the account number
        if self.l10n_ch_qr_iban:
            qr_vals[3] = sanitize_account_number(self.l10n_ch_qr_iban)
        return qr_vals
