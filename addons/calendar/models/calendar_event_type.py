# -*- coding: utf-8 -*-
# Part of Odoo, Flectra, Sleektiv. See LICENSE file for full copyright and licensing details.

from sleektiv import fields, models


class MeetingType(models.Model):

    _name = 'calendar.event.type'
    _description = 'Event Meeting Type'

    name = fields.Char('Name', required=True)

    _sql_constraints = [
        ('name_uniq', 'unique (name)', "Tag name already exists !"),
    ]
