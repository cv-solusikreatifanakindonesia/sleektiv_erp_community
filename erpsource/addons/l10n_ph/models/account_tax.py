# Part of Odoo, Flectra. See LICENSE file for full copyright and licensing details.

from flectra import fields, models


class AccountTax(models.Model):
    _inherit = "account.tax"

    l10n_ph_atc = fields.Char("Philippines ATC")
