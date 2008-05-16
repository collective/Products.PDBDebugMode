PDBDebugMode - Enable various PDB debugging when debug-mode=on

When Zope is running in debug mode this product enables post-mortem
debugging on exceptions, runcall debugging of designated requests, and
import of pdb in unprotected code.

REQUIREMENTS:

PDBDebugMode has only been tested with Zope 2.8.5 and 2.10
SVN/UNRELEASED but may well work with other versions.

Its recommended that you use an editor or IDE that can cooperate with
pdb. Emacs' gud-mode, for example, will display the corresponding
lines of the source file alongside the pdb prompt.

INSTALLATION:

Just put the PDBDebugMode directory into any of your instances
Products directories and restart Zope.

Remember that this product does nothing unless zope is being run with
debug-mode=on such as with "instance/bin/zopectl fg"

POST-MORTEM DEBUGGING:

If Zope is running with debug-mode=on and this product is installed,
upon raising any valid exception the port-mortem debugger is invoked
with the traceback.  Once in the debugger you can examine objects,
variables, etc. at all levels of the call stack.  This is, of course,
extremely useful for debugging.

Valid exceptions for post-mortem debugging are determined as follows.
If a relevant error log object is found, exceptions included in the
error log's ignored exception types will be ignored and the debugger
won't be invoked.  All ZODB Conflict and Zope Retry errors are also
ignored.

RUNCALL REQUESTS:

If Zope is running with debug-mode=on and this product is installed,
any request that has the key "pdb_runcall" will call the result of the
request traversal in the debugger thus allowing for stepping through
the resulting execution.

Alternatively, a view named 'pdb' is registered for all objects that
will simply raise an exception leaving you with the current context to
inspect.

ALLOW IMPORT OF PDB:

If Zope is running with debug-mode=on and this product is installed,
import of the pdb module is allowed in unprotected code such as python
scripts.
