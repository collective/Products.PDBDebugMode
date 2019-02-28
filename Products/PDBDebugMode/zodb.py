from ZODB import Connection
from ZODB.serialize import ObjectWriter

orig_register = Connection.Connection.register


def register(self, obj):
    """
    Serialize early to inspect PicklingErrors

    Raise any PicklingErrors when the object is added to the
    transaction as opposed to when the transaction is committed.
    Under pdb, for example, this allows inspecting the code that made
    the change resulting in the PicklingError.

    Requires either zope.testrunner or zope.testing which can be included using
    the 'zodb' or 'zodb-testing' extras respectively.
    """
    orig_register(self, obj)

    writer = ObjectWriter(obj)

    # Replace the pickler so that it doesn't set oids
    import six.moves.cPickle as pickle
    writer._p = pickle.Pickler(writer._file, 1)

    # Try to serialize to raise piclkling errors early
    writer.serialize(obj)
