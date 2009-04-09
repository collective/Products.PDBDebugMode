"""Hook the logger.error call."""

import sys
import re
import logging
from pdb import set_trace
from pdb import post_mortem

logger = logging.getLogger('Products.PDBDebugMode')

LoggerClass = logging.getLoggerClass()
orig_error = LoggerClass.error

ignore_matchers = (
    # There's a known error in ZCatalog where deleting a container
    # will generate these log errors for its children
    re.compile(
        '^uncatalogObject unsuccessfully attempted to uncatalog an '
        'object with a uid of ').search,
    )

def error(self, msg, *args, **kw):
    """Drop into pdb when logging an error."""
    result = orig_error(self, msg, *args, **kw)

    for matcher in ignore_matchers:
        try:
            match = matcher(msg)
        except:
            logger.exception('Matcher %r failed for log message %r' %
                             (matcher, msg))
        if match:
            break
    else:
        type, value, traceback = sys.exc_info()
        if traceback is None:
            set_trace()
        else:
            # When the logger is invoked inside a try block, do
            # post_mortem debugging on the error
            post_mortem(traceback)
        
    return result
