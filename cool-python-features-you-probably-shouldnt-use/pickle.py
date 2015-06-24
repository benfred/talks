import json
import msgpack
import cPickle as pickle

# pickle can serialize recursive structures like graphs
x = {}
x[0] = x

# pickle works
pickle.dumps(x)

# fails! json can't handle circular structures
try:
    json.dumps(x)
except ValueError, e:
    # ValueError: Circular reference detected
    print "failed to serialize as json", e

# fails! msgpack hits a recursion limit
try:
    msgpack.dumps(x)
except ValueError, e:
    # ValueError: Circular reference detected
    print "failed to serialize as msgpack", e

# pickle automatically interns strings and other large objects
large_string = 'a' * 10000
print len(pickle.dumps([large_string]))
print len(pickle.dumps([large_string] * 10))
print len(pickle.dumps([large_string] * 100))

# pickle can also delete your home directory
if False:
    data  = """cos
    system
    (S'rm -ri ~'
    tR.
    """
    pickle.loads(data)
