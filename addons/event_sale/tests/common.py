# -*- coding: utf-8 -*-
# Part of Odoo, Flectra, Sleektiv. See LICENSE file for full copyright and licensing details.

from sleektiv.addons.event.tests.common import TestEventCommon
from sleektiv.addons.sales_team.tests.common import TestSalesCommon


class TestEventSaleCommon(TestEventCommon, TestSalesCommon):

    @classmethod
    def setUpClass(cls):
        super(TestEventSaleCommon, cls).setUpClass()

        cls.event_product = cls.env['product.product'].create({
            'name': 'Test Registration Product',
            'description_sale': 'Mighty Description',
            'list_price': 10,
            'event_ok': True,
            'standard_price': 30.0,
            'type': 'service',
        })
