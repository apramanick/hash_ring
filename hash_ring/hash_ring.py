# -*- coding: utf-8 -*-
"""
    hash_ring
    ~~~~~~~~~~~~~~
    Implements consistent hashing that can be used when
    the number of server nodes can increase or decrease (like in memcached).

    Consistent hashing is a scheme that provides a hash table functionality
    in a way that the adding or removing of one slot does not significantly
    change the mapping of keys to slots.

    Example of usage::

        servers = ['192.168.0.246:11212',
                   '192.168.0.247:11212',
                   '192.168.0.249:11212']

        ring = HashRing(servers)
        server = ring.get_node('my_key')

    :copyright: 2008 by Amir Salihefendic.
    :license: MIT
"""

import math
import sys
from bisect import bisect

if sys.version_info >= (2, 5):
    import hashlib
    _MD5_CTOR = hashlib.md5
else:
    # noinspection PyUnresolvedReferences
    import md5
    _MD5_CTOR = md5.new


class HashRing(object):

    def __init__(self, nodes=None, weights=None):
        """`nodes` is a list of objects that have a proper __str__ representation.
        `weights` is dictionary that sets weights to the nodes.  The default
        weight is that all nodes are equal.
        """
        self.ring = dict()
        self._sorted_keys = []

        self.nodes = nodes

        if not weights:
            weights = {}
        self.weights = weights

        self._generate_circle()

    def _generate_circle(self):
        """Generates the circle.
        """
        total_weight = 0
        for node in self.nodes:
            total_weight += self.weights.get(node, 1)

        for node in self.nodes:
            weight = 1

            if node in self.weights:
                weight = self.weights.get(node)

            factor = math.floor((40 * len(self.nodes) * weight) / total_weight)

            for j in range(0, int(factor)):
                b_key = self._hash_digest('%s-%s' % (node, j))
                for i in range(0, 3):
                    key = self._hash_val(b_key, lambda x: x + i * 4)
                    self.ring[key] = node
                    self._sorted_keys.append(key)

        self._sorted_keys.sort()

    def get_node(self, string_key):
        """Given a string key a corresponding node in the hash ring is returned.

        If the hash ring is empty, `None` is returned.
        """
        pos = self.get_node_pos(string_key)
        if pos is None:
            return None
        return self.ring[self._sorted_keys[pos]]

    def get_node_pos(self, string_key):
        """Given a string key a corresponding node in the hash ring is returned
        along with it's position in the ring.

        If the hash ring is empty, (`None`, `None`) is returned.
        """
        if not self.ring:
            return None

        key = self.gen_key(string_key)

        nodes = self._sorted_keys
        pos = bisect(nodes, key)

        if pos == len(nodes):
            return 0
        else:
            return pos

    # noinspection PyUnusedLocal
    def iterate_nodes(self, string_key, distinct=True):
        """Given a string key it returns the nodes as a generator that can hold the key.

        The generator iterates one time through the ring
        starting at the correct position.

        if `distinct` is set, then the nodes returned will be unique,
        i.e. no virtual copies will be returned.
        """
        if not self.ring:
            yield None, None

        returned_values = set()

        def distinct_filter(value):
            if str(value) not in returned_values:
                returned_values.add(str(value))
                return value

        pos = self.get_node_pos(string_key)
        for key in self._sorted_keys[pos:]:
            val = distinct_filter(self.ring[key])
            if val:
                yield val

        for i, key in enumerate(self._sorted_keys):
            if i < pos:
                val = distinct_filter(self.ring[key])
                if val:
                    yield val

    def gen_key(self, key):
        """Given a string key it returns a long value,
        this long value represents a place on the hash ring.

        md5 is currently used because it mixes well.
        """
        b_key = self._hash_digest(key)
        return self._hash_val(b_key, lambda x: x)

    @staticmethod
    def _hash_val(b_key, entry_fn):
        return ((b_key[entry_fn(3)] << 24)
                | (b_key[entry_fn(2)] << 16)
                | (b_key[entry_fn(1)] << 8)
                | b_key[entry_fn(0)])

    @staticmethod
    def _hash_digest(key):
        if int(sys.version_info.major) >= 3:
            # In Python 3, all strings comprise Unicode code-points internally.  So, the
            # key, which is a string, needs to be encoded before it can be hashed:
            enc_key = key.encode('UTF-8')
        else:
            enc_key = key

        # Create a fresh md5 algorithm object:
        m = _MD5_CTOR()
        m.update(enc_key)

        if int(sys.version_info.major) >= 3:
            # In Python 3, m.digest() already returns bytes (and not a string, as in Python 2).
            # Hence, we can simply return the digest as-is; however, to mimic as closely as
            # possible what the Python 2.x code does, we return a bytearray of the digest:
            return bytearray(m.digest())
        else:
            return map(ord, m.digest())
