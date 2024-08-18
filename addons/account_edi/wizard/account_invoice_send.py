# -*- coding: utf-8 -*-
# Part of Odoo, Flectra, Sleektiv. See LICENSE file for full copyright and licensing details.

from sleektiv import api, fields, models, _
from sleektiv.exceptions import UserError
import base64


class AccountInvoiceSend(models.TransientModel):
    _inherit = 'account.invoice.send'
    _description = 'Account Invoice Send'

    edi_format_ids = fields.Many2many(related='invoice_ids.journal_id.edi_format_ids', string="Electronic invoicing")
