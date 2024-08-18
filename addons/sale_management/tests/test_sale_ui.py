import sleektiv.tests
# Part of Odoo, Flectra, Sleektiv. See LICENSE file for full copyright and licensing details.


@sleektiv.tests.tagged('post_install', '-at_install')
class TestUi(sleektiv.tests.HttpCase):

    def test_01_sale_tour(self):
        self.start_tour("/web", 'sale_tour', login="admin", step_delay=100)
