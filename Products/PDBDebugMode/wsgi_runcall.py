try:
    import ipdb as pdb
except ImportError:
    import pdb


def resolveDottedName(dotted_name):
    """Resolve the dotted name importing as necessary then using
    getattr."""
    idx = dotted_name.find('.')
    if idx == -1:
        base_name = dotted_name
        rest_path = []
    else:
        base_name = dotted_name[:idx]
        rest_path = dotted_name[idx + 1:].split('.')

    obj = __import__(base_name)

    for name in rest_path:
        obj = getattr(obj, name)

    return obj


def pdb_runcall(obj, args, request):
    """If the request has the pdb_runcall key then we run the result
    of request traversal in the debugger.  Othwise, do it normally.

    A cookie for pdb_runcall may also be set or removed if the request
    has the toggle_runcall key."""
    response = request.response

    if 'toggle_runcall' in request and request.toggle_runcall:
        runcall_cookie = request.cookies.get('pdb_runcall', False)
        if runcall_cookie:
            response.expireCookie('pdb_runcall')
            return obj(*args)
        else:
            response.setCookie('pdb_runcall', 1)

    if 'set_runcall_ignore' in request:
        if request.set_runcall_ignore:
            for ignore in request.set_runcall_ignore:
                response.appendCookie('runcall_ignore', ignore)
        else:
            response.expireCookie('runcall_ignore')

    if 'pdb_runcall' in request:
        if request.pdb_runcall:
            ignores = request.get('runcall_ignore', [])
            if ignores:
                ignores = ignores.split(':')
            for ignore in ignores:
                _obj = resolveDottedName(ignore)
                if _obj.__func__ is getattr(obj, 'im_func', None):
                    break
            else:
                return pdb.runcall(obj, *args)
    return obj(*args)
