import sys


def is_enabled():
    try:
        from App.config import getConfiguration
        debug_mode = getConfiguration().debug_mode
    except:
        debug_mode = False
    if debug_mode:
        return True

    try:
        from zope import testrunner
        from zope.testrunner import options
    except ImportError:
        from zope.testing import testrunner
        from zope.testing.testrunner import options
    frame = sys._getframe(2)
    while frame is not None and frame.f_code is not testrunner.run.func_code:
        frame = frame.f_back
    if frame is not None:
        try:
            pm = options.get_options().post_mortem
            return bool(pm)
        except:
            # options not recognized by test runnergiven
            pass

    return False
