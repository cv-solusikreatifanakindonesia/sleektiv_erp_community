# -*- coding: utf-8 -*-
# Part of Odoo, Flectra, Sleektiv. See LICENSE file for full copyright and licensing details.

from sleektiv import models


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    def _sms_get_number_fields(self):
        """ This method returns the fields to use to find the number to use to
        send an SMS on a record. """
        # TDE FIXME: to be cleaned in 14.4+ as it conflicts with _phone_get_number_fields
        return ['mobile', 'phone']
