"""If debug-mode=on, Monkey-patch the zpublisher_exception_hook to
call pdb.post_mortem on an error and enable import of pdb in
unprotected code.
"""

#XXX Look into a Zope Five solution

from types import StringType

from Zope2.App import startup
from ZPublisher import Publish
from ZPublisher.Publish import missing_name
from ZPublisher.Publish import dont_publish_class
from ZPublisher.Publish import mapply
from Globals import DevelopmentMode
from AccessControl import allow_module

try:
    from Products.PlacelessTranslationService import PatchStringIO
except ImportError:
    from ZPublisher.Publish import publish as real_publish
    USE_PTS = False
else:
    USE_PTS = True
    from ZPublisher.Publish import old_publish as real_publish
    

from pdbzope.exceptionhook import pdb_exception_hook
from pdbzope.runcall import pdb_runcall

import logging
log = logging.getLogger('PDBDebugMode')

# XXX Check for PlacelessTranslationService monkeypatch

def pdb_publish(request, module_name, after_list, debug=0,
                call_object=pdb_runcall,
                missing_name=missing_name,
                dont_publish_class=dont_publish_class,
                mapply=mapply, ):
    """Hook the publish function to override the function used to call
    the result of the request traversal."""
    return real_publish(request, module_name, after_list, debug=0,
                call_object=call_object,
                missing_name=missing_name,
                dont_publish_class=dont_publish_class,
                mapply=mapply, )

if DevelopmentMode:

    # call pdb.post_mortem on an error
    # startup.zpublisher_exception_hook = pdb_exception_hook

    # call pdb.runcall when the final call for a request is done
    if USE_PTS:
        Publish.zpublisher_publish = Publish.old_publish
        Publish.old_publish = pdb_publish
    else:
        Publish.old_publish = Publish.publish
        Publish.publish = pdb_publish

    # Allow import of pdb in unprotected code
    allow_module('pdb')

    # Import modules that monkey patch various code to prevent it from
    # swallowing exceptions
    for module in ('pdblogging', 'cmfplone', 'archetypes', 'atct', 'zcatalog'):
        try:
            __import__('Products.PDBDebugMode.%s' % module)
        except ImportError:
            log.info('Failed to monkey patch %s' % module)
