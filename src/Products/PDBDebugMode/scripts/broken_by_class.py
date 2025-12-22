from OFS import Uninstalled

import pprint


broken = {}
for path, obj in app.ZopeFind(app, search_sub=True):  # noqa: F821
    if isinstance(obj, Uninstalled.BrokenClass):
        broken.setdefault(obj.__class__, []).append(path)


pprint.pprint(broken)
