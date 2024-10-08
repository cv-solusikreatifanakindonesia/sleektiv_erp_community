# Part of sleektiv. See LICENSE file for full copyright and licensing details.

from sleektiv import fields, models


class HelpdeskTeam(models.Model):
    _inherit = 'helpdesk.team'

    forum_id = fields.Many2one('forum.forum', string="Forum", store=True)
