"""Call pdb.post_mortem on an error. Check the error_log
configuration if available and do not call pdb.post_moretm for
excluded error types.
"""

import pdb
import logging
import ZPublisher
from Acquisition import aq_acquire
from ZODB.POSException import ConflictError
from Zope2.App.startup import zpublisher_exception_hook

LOG = logging.getLogger('PDBDebugMode')

error_type = type(ConflictError)

def pdb_exception_inner(published, t, traceback):

    try:
        # Check the error log for ignored error types
        try:
            log = aq_acquire(published, '__error_log__', containment=1)
        except AttributeError:
            ignored_exceptions = ()
        else:
            ignored_exceptions = log.getProperties()['ignored_exceptions']
        strtype = str(getattr(t, '__name__', t))

        # Suppliment ignored exceptions with ConflictError and Retry
        # which zpublisher_exception_hook handles
        if not (strtype in ignored_exceptions or
                t is ZPublisher.Retry or
                (type(t) == error_type and
                issubclass(t, ConflictError))):
            pdb.post_mortem(traceback)
            # resume normal error handling if continue is given to pdb

    except:
        # Globally catch errors in our code and log them so as not to
        # disrupt proper error handling
        LOG.error('post-mortem debugging raised an error', exc_info=True)

def pdb_exception_hook(published, REQUEST, t, v, traceback):
    """Call pdb.post_mortem on an error.  Check the error_log
    configuration if available and do not call pdb.post_moretm for
    excluded error types.
    """

    # Do our actual post-mortem handling in a separate function so it
    # gets called in an inner frame and won't interfere with
    # sys.exc_info if our code generates an error
    pdb_exception_inner(published, t, traceback)

    # Resume normal error handling
    return zpublisher_exception_hook(published, REQUEST, t, v, traceback)
