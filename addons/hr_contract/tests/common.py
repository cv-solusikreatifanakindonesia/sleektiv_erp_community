# -*- coding: utf-8 -*-
# Part of Odoo, Flectra, Sleektiv. See LICENSE file for full copyright and licensing details.

from sleektiv.tests.common import SavepointCase


class TestContractCommon(SavepointCase):

    @classmethod
    def setUpClass(cls):
        super(TestContractCommon, cls).setUpClass()

        cls.employee = cls.env['hr.employee'].create({
            'name': 'Richard',
            'gender': 'male',
            'country_id': cls.env.ref('base.be').id,
        })
