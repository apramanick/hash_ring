#
# BSD 2-Clause License
#
# Copyright (c) 2007 Amir Salihefendic
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, this
# list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
# this list of conditions and the following disclaimer in the documentation
# and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
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
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
      ],
      packages=['hash_ring'],
      platforms=["Any"],
      license="BSD",
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
