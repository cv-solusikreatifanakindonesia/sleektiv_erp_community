# Part of Odoo, Flectra, Sleektiv. See LICENSE file for full copyright and licensing details.

from sleektiv.addons.base.tests.common import HttpCaseWithUserDemo, TransactionCaseWithUserDemo


class HttpCaseGamification(HttpCaseWithUserDemo):

    def setUp(self):
        super().setUp()
        if not self.user_demo.karma:
            self.user_demo.karma = 2500


class TransactionCaseGamification(TransactionCaseWithUserDemo):

    def setUp(self):
        super().setUp()
        if not self.user_demo.karma:
            self.user_demo.karma = 2500
