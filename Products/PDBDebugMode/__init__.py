"""If debug-mode=on, Monkey-patch the zpublisher_exception_hook to
call pdb.post_mortem on an error and enable import of pdb (and ipdb) in
unprotected code.
"""

import sys

import Globals
import AccessControl

from Products.PDBDebugMode import debugger

if debugger.is_enabled():
    sys.modules['Products.PDBDebugMode.Globals'] = Globals

    # Allow import of pdb in unprotected code
    AccessControl.allow_module('pdb')
    AccessControl.allow_module('ipdb')

    AccessControl.allow_module('Products.PDBDebugMode.debugger')
