# -*- coding: utf-8 -*-
# Part of Odoo, Flectra, Sleektiv. See LICENSE file for full copyright and licensing details.

import sleektiv.tests
from sleektiv.tools import mute_logger


@sleektiv.tests.common.tagged('post_install', '-at_install')
class TestCustomSnippet(sleektiv.tests.HttpCase):

    @mute_logger('sleektiv.addons.http_routing.models.ir_http', 'sleektiv.http')
    def test_01_run_tour(self):
        self.start_tour("/", 'test_custom_snippet', login="admin")
