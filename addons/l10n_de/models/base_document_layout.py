from sleektiv import models, fields, _
from sleektiv.tools import format_date


class BaseDocumentLayout(models.TransientModel):
    _inherit = 'base.document.layout'

    street = fields.Char(related='company_id.street', readonly=True)
    street2 = fields.Char(related='company_id.street2', readonly=True)
    zip = fields.Char(related='company_id.zip', readonly=True)
    city = fields.Char(related='company_id.city', readonly=True)
    company_registry = fields.Char(related='company_id.company_registry', readonly=True)
    bank_ids = fields.One2many(related='company_id.partner_id.bank_ids', readonly=True)
    l10n_de_template_data = fields.Binary(compute='_compute_l10n_de_template_data')
    l10n_de_document_title = fields.Char(compute='_compute_l10n_de_document_title')

    def _compute_l10n_de_template_data(self):
        self.l10n_de_template_data = [
            (_("Invoice No."), 'INV/2021/12345'),
            (_("Invoice Date"), format_date(self.env, fields.Date.today())),
            (_("Due Date"), format_date(self.env, fields.Date.add(fields.Date.today(), days=7))),
            (_("Reference"), 'SO/2021/45678'),
        ]

    def _compute_l10n_de_document_title(self):
        self.l10n_de_document_title = 'Invoice'
