# Part of Odoo, Flectra, Sleektiv. See LICENSE file for full copyright and licensing details.

import sleektiv.tests


@sleektiv.tests.tagged('post_install', '-at_install')
class TestUi(sleektiv.tests.HttpCase):

    def test_01_project_tour(self):
        self.start_tour("/web", 'project_tour', login="admin")
