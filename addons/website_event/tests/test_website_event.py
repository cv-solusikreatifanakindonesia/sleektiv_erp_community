# -*- coding: utf-8 -*-
# Part of Odoo, Flectra, Sleektiv. See LICENSE file for full copyright and licensing details.

from sleektiv.addons.website.tests.test_base_url import TestUrlCommon
from sleektiv.tests import tagged


@tagged('-at_install', 'post_install')
class TestUrlCanonical(TestUrlCommon):

    def test_01_canonical_url(self):
        self._assertCanonical('/event?date=all', self.domain + '/event')
        self._assertCanonical('/event?date=old', self.domain + '/event?date=old')
