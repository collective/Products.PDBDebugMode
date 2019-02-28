"""If debug-mode=on, Monkey-patch the zpublisher_exception_hook to
call pdb.post_mortem on an error and enable import of pdb (and ipdb) in
unprotected code.
"""

import sys
from types import ModuleType
import AccessControl

from Products.PDBDebugMode import debugger

try:
    from ZPublisher.Publish import publish
    ZOPE2 = True
except:
    try:
        from ZServer.ZPublisher.Publish import publish
        ZOPE2 = True
    except:
        ZOPE2 = False


if debugger.is_enabled():
    if ZOPE2:
        z2_enabled = ModuleType('z2_enabled')
        sys.modules['Products.PDBDebugMode.z2_enabled'] = z2_enabled
    else:
        z4_enabled = ModuleType('z4_enabled')
        sys.modules['Products.PDBDebugMode.z4_enabled'] = z4_enabled

    # Allow import of pdb in unprotected code
    AccessControl.allow_module('pdb')
    AccessControl.allow_module('ipdb')

    AccessControl.allow_module('Products.PDBDebugMode.debugger')
