# -*- coding: utf-8 -*-
# Part of Odoo, Flectra, Sleektiv. See LICENSE file for full copyright and licensing details.

from sleektiv import models


class AccountPayment(models.Model):
    _inherit = 'account.payment'

    def action_retry_edi_documents_error(self):
        self.ensure_one()
        return self.move_id.action_retry_edi_documents_error()
