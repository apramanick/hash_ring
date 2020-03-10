#
# MIT License
#
# Copyright (c) 2020 Ankan Pramanick
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
"""
A very rough and quick sanity test for the hash_ring port to Python 3.8.

This is by no means a unit test for the hash_ring module.  Rather, it simply allows
one to compare the output (over a very small input set) of the Python 2.x code versus
the code as ported to Python 3.8.

See ./test_port.sh for details on how to run this test.
"""
import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), "../hash_ring"))

from hash_ring import HashRing


def main():
    servers = [
        '192.168.0.235',
        '192.168.0.237',
        '192.168.0.239',
        '192.168.0.241',
        '192.168.0.243',
        '192.168.0.245',
        '192.168.0.247',
        '192.168.0.249'
    ]
    keys = [
        "my_key",
        "FooBarBaz",
        "my_key",
        "FooBarBaz",
        "_01234567890-",
        "_01234567890-",
        "@#$%^&*!()[]{}",
        "timekeeper",
        "highball",
        "ponytail",
        "candlestick",
        "watermelon",
        "timepieces",
        "forewarn",
        "newborn",
        "firebreak",
        "disk drive",
        "warehouse",
        "forget",
        "bypass",
        "crossbow",
        "supernatural",
        "paul-frederic-simon",
        "deprive",
        "gregarious",
        "procrastination",
        "suffice"
    ]
    weights = {
        '192.168.0.235': 1,
        '192.168.0.237': 2,
        '192.168.0.239': 1,
        '192.168.0.241': 1,
        '192.168.0.243': 1,
        '192.168.0.245': 2,
        '192.168.0.247': 1,
        '192.168.0.249': 3
    }

    ring = HashRing(servers)
    for key in keys:
        server = ring.get_node(key)
        print(server)

    ring = HashRing(servers, weights)
    for key in keys:
        server = ring.get_node(key)
        print(server)


if __name__ == "__main__":
    sys.exit(main())
