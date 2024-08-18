from sleektiv import api, fields, models, modules, tools, _

class IrModuleModule(models.Model):
    _inherit = "ir.module.module"

    license = fields.Selection(selection_add=[('FPL-1', 'Sleektiv Proprietary License v1.0'),
                                              ('FPEL-1', 'Sleektiv Professional Edition License v1.0'),
                                              ])
