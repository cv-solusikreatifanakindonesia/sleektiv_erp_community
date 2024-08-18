# -*- coding: utf-8 -*-
# Part of Odoo, Flectra, Sleektiv. See LICENSE file for full copyright and licensing details.

import sleektiv.tests
from sleektiv import tools


@sleektiv.tests.tagged('post_install', '-at_install')
class TestUi(sleektiv.tests.HttpCase):
    def test_admin(self):
        self.start_tour("/", 'event', login='admin', step_delay=100)
