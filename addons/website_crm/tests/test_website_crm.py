# -*- coding: utf-8 -*-
# Part of Odoo, Flectra, Sleektiv. See LICENSE file for full copyright and licensing details.

import sleektiv.tests


@sleektiv.tests.tagged('post_install', '-at_install')
class TestWebsiteCrm(sleektiv.tests.HttpCase):

    def test_tour(self):
        self.start_tour("/", 'website_crm_tour')

        # check result
        record = self.env['crm.lead'].search([('description', '=', '### TOUR DATA ###')])
        self.assertEqual(len(record), 1)
        self.assertEqual(record.contact_name, 'John Smith')
        self.assertEqual(record.email_from, 'john@smith.com')
        self.assertEqual(record.partner_name, 'Sleektiv, FlectraHQ, Inc., Odoo S.A.')
