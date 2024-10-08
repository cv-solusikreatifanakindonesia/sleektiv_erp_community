# -*- coding: utf-8 -*-
# Part of Odoo, Flectra, Sleektiv. See LICENSE file for full copyright and licensing details.

from sleektiv import fields, models


class Lead(models.Model):
    _inherit = 'crm.lead'

    reveal_ip = fields.Char(string='IP Address')
    reveal_iap_credits = fields.Integer(string='IAP Credits')
    reveal_rule_id = fields.Many2one('crm.reveal.rule', string='Lead Generation Rule', index=True)
