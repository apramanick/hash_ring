# hash_ring

A clone of the last published version (version 1.3.1) of Python hash_ring from PyPi.
I created this clone since we needed to continue using the original project in Python
3.x, and the original had stopped being maintained, and was stuck at Python 2.x.

The only modifications I have made is to port this to Python 3.8, and remove the
memcache_ring module, since I never use it, and it was not practical for me to test
it out.

Currently, I have no plans to support this long-term, since this is a temporary
measure to port our own code to Python 3.x as painlessly as possible; in fiture,
we might move to using a different Python consistent hashing implementation,
at which time I will drop support for this.

The following description is mostly from the original package.


# About hash_ring

Implements consistent hashing that can be used when
the number of server nodes can increase or decrease (like in memcached).
The hashing ring is built using the same algorithm as libketama.

Consistent hashing is a scheme that provides a hash table functionality
in a way that the adding or removing of one slot
does not significantly change the mapping of keys to slots.

More information about consistent hashing can be read in these articles:

* [Web Caching with Consistent Hashing](http://www.cs.cmu.edu/~srini/15-744/S02/readings/K+99.html)
* [Consistent hashing and random trees](http://citeseerx.ist.psu.edu/legacymapper?did=38148)


# Examples

Basic example of usage:

    servers = ['192.168.0.246:11212',
               '192.168.0.247:11212',
               '192.168.0.249:11212']

    ring = HashRing(servers)
    server = ring.get_node('my_key')

Example using weights:

    servers = ['192.168.0.246:11212',
               '192.168.0.247:11212',
               '192.168.0.249:11212']
    weights = {
        '192.168.0.246:11212': 1,
        '192.168.0.247:11212': 2,
        '192.168.0.249:11212': 1
    }

    ring = HashRing(servers, weights)
    server = ring.get_node('my_key')

# Installation

    $ git clone https://github.com/apramanick/hash_ring.git
    $ cd hash_ring
    $ pip3.8 install .

