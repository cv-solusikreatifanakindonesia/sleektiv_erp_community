# -*- coding: utf-8 -*-
# Part of Odoo, Flectra, Sleektiv. See LICENSE file for full copyright and licensing details.

import json
import logging
import pprint

from sleektiv import http
from sleektiv.http import request

_logger = logging.getLogger(__name__)


class SleektivByAdyenController(http.Controller):
    _notification_url = '/payment/sleektiv_adyen/notification'

    @http.route('/payment/sleektiv_adyen/notification', type='json', auth='public', csrf=False)
    def sleektiv_adyen_notification(self):
        data = json.loads(request.httprequest.data)
        _logger.info('Beginning Sleektiv by Adyen form_feedback with data %s', pprint.pformat(data)) 
        if data.get('authResult') not in ['CANCELLED']:
            request.env['payment.transaction'].sudo().form_feedback(data, 'sleektiv_adyen')
