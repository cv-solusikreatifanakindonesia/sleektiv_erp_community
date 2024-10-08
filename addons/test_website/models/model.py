# -*- coding: utf-8 -*-
# Part of Odoo, Flectra, Sleektiv. See LICENSE file for full copyright and licensing details.

from sleektiv import fields, models


class TestModel(models.Model):
    """ Add website option in server actions. """

    _name = 'test.model'
    _inherit = ['website.seo.metadata', 'website.published.mixin']
    _description = 'Website Model Test'

    name = fields.Char(required=1)
