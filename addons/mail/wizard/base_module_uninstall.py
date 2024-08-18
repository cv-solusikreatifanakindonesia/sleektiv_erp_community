# -*- coding: utf-8 -*-
# Part of Odoo, Flectra, Sleektiv. See LICENSE file for full copyright and licensing details.

from sleektiv import models


class BaseModuleUninstall(models.TransientModel):
    _inherit = "base.module.uninstall"

    def _get_models(self):
        # consider mail-thread models only
        models = super(BaseModuleUninstall, self)._get_models()
        return models.filtered('is_mail_thread')
