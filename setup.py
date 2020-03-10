#
# MIT License
# 
# Copyright (c) 2007 Amir Salihefendic
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
import os

from setuptools import setup


def list_files(path):
    for fn in os.listdir(path):
        if fn.startswith('.'):
            continue
        fn = os.path.join(path, fn)
        if os.path.isfile(fn):
            yield fn


setup(name='hash_ring',
      version='1.4.0',
      author="Amir Salihefendic",
      author_email="amix@amix.dk",
      url="http://www.amix.dk/",
      classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
      ],
      packages=['hash_ring'],
      platforms=["Any"],
      license="MIT",
      keywords='hashing hash consistent',
      description="Implements consistent hashing in Python (using md5 as hashing function).",
      long_description="""\
About hash_ring
---------------

Implements consistent hashing that can be used when
the number of server nodes can increase or decrease (like in memcached).
The hashing ring is built using the same algorithm as libketama.

Consistent hashing is a scheme that provides a hash table functionality
in a way that the adding or removing of one slot
does not significantly change the mapping of keys to slots.

More information about consistent hashing can be read in these articles:

* Web Caching with Consistent Hashing <http://www.cs.cmu.edu/~srini/15-744/S02/readings/K+99.html>
* Consistent hashing and random trees <http://citeseerx.ist.psu.edu/legacymapper?did=38148>


Example
-------

Basic example of usage::

    servers = ['192.168.0.246:11212',
               '192.168.0.247:11212',
               '192.168.0.249:11212']

    ring = HashRing(servers)
    server = ring.get_node('my_key')

Example using weights::

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

""")
