"""If debug-mode=on enable import of pdb (and ipdb) in
unprotected code.
"""
from AccessControl import allow_module
from Products.PDBDebugMode import debugger
from types import ModuleType

import sys
import logging

log = logging.getLogger(__name__)


if debugger.is_enabled():
    enabled = ModuleType('enabled')
    sys.modules['Products.PDBDebugMode.enabled'] = enabled
    warning = ("""

******************************************************************************

Debug-Mode enabled!

This will result in a pdb when a exception happens.
Turn off debug mode or remove Products.PDBDebugMode to disable.

See https://pypi.python.org/pypi/Products.PDBDebugMode

******************************************************************************
""")

    log.warning(warning)
    # Allow import of pdb in unprotected code
    allow_module('pdb')
    allow_module('ipdb')
    allow_module('Products.PDBDebugMode.debugger')
