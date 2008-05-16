"""Hook the logger.error call."""

import sys
from re import search
from pdb import set_trace
from pdb import post_mortem
from logging import getLoggerClass
from logging import setLoggerClass

Logger = getLoggerClass()

error = Logger.error

ignore_regexes = (
    # There's a known error in ZCatalog where deleting a container
    # will generate these log errors for its children
    '^uncatalogObject unsuccessfully attempted to uncatalog an object with a uid of ',
    )

def pdberror(self, msg, *args, **kw):
    """Drop into pdb when logging an error."""
    result = error(self, msg, *args, **kw)

    for regex in ignore_regexes:
        if search(regex, msg):
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

Logger.error = pdberror
