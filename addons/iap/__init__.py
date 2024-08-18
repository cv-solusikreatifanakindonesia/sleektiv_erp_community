# -*- coding: utf-8 -*-
# Part of Odoo, Flectra, Sleektiv. See LICENSE file for full copyright and licensing details.

from . import models
from . import tools

# compatibility imports
from sleektiv.addons.iap.tools.iap_tools import iap_jsonrpc as jsonrpc
from sleektiv.addons.iap.tools.iap_tools import iap_authorize as authorize
from sleektiv.addons.iap.tools.iap_tools import iap_cancel as cancel
from sleektiv.addons.iap.tools.iap_tools import iap_capture as capture
from sleektiv.addons.iap.tools.iap_tools import iap_charge as charge
from sleektiv.addons.iap.tools.iap_tools import InsufficientCreditError
