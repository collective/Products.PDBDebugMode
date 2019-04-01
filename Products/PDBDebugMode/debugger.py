# -*- coding: utf-8 -*-
def is_enabled():
    try:
        from App.config import getConfiguration
        debug_mode = getConfiguration().debug_mode
    except Exception:
        debug_mode = False
    return debug_mode
