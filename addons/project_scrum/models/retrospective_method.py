# Part of Odoo, Flectra, Sleektiv. See LICENSE file for full copyright and licensing details.

from sleektiv import models, fields


class RetrospectiveMethod(models.Model):
    _name = "retrospective.method"
    _inherit = 'mail.thread'
    _description = "Retrospective Implementation for Project Scrum"

    name = fields.Char(
        string="Method Name", required=True, tracking=True)

    description = fields.Text(
        string="Description", tracking=True)
