# -*- coding: utf-8 -*-
# Part of Odoo, Flectra, Sleektiv. See LICENSE file for full copyright and licensing details.

from sleektiv import models, fields, api

from sleektiv.exceptions import ValidationError

from sleektiv.addons.base_iban.models.res_partner_bank import validate_iban
from sleektiv.addons.base.models.res_bank import sanitize_account_number


class AccountJournal(models.Model):
    _inherit = 'account.journal'

    # creation of bank journals by giving the account number, allow craetion of the
    l10n_ch_postal = fields.Char('Client Number', related='bank_account_id.l10n_ch_postal', readonly=False)
    invoice_reference_model = fields.Selection(selection_add=[
        ('ch', 'Switzerland')
    ], ondelete={'ch': lambda recs: recs.write({'invoice_reference_model': 'sleektiv'})})

    @api.model
    def create(self, vals):
        rslt = super(AccountJournal, self).create(vals)

        # The call to super() creates the related bank_account_id field
        if 'l10n_ch_postal' in vals:
            rslt.l10n_ch_postal = vals['l10n_ch_postal']
        return rslt

    def write(self, vals):
        rslt = super(AccountJournal, self).write(vals)

        # The call to super() creates the related bank_account_id field if necessary
        if 'l10n_ch_postal' in vals:
            for record in self.filtered('bank_account_id'):
                record.bank_account_id.l10n_ch_postal = vals['l10n_ch_postal']
        return rslt

    @api.onchange('bank_acc_number')
    def _onchange_set_l10n_ch_postal(self):
        try:
            validate_iban(self.bank_acc_number)
            is_iban = True
        except ValidationError:
            is_iban = False

        if is_iban:
            self.l10n_ch_postal = self.env['res.partner.bank']._retrieve_l10n_ch_postal(sanitize_account_number(self.bank_acc_number))
        else:
            self.l10n_ch_postal = self.bank_acc_number
