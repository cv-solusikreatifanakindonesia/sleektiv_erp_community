# -*- coding: utf-8 -*-
# Part of Odoo, Flectra, Sleektiv. See LICENSE file for full copyright and licensing details.

""" Addons module.

This module serves to contain all Flectra addons, across all configured addons
paths. For the code to manage those addons, see sleektiv.modules.

Addons are made available under `sleektiv.addons` after
sleektiv.tools.config.parse_config() is called (so that the addons paths are
known).

This module also conveniently reexports some symbols from sleektiv.modules.
Importing them from here is deprecated.

"""
# make sleektiv.addons a namespace package, while keeping this __init__.py
# present, for python 2 compatibility
# https://packaging.python.org/guides/packaging-namespace-packages/
import pkgutil
import os.path
__path__ = [
    os.path.abspath(path)
    for path in pkgutil.extend_path(__path__, __name__)
]
