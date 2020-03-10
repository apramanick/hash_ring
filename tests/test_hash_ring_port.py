#
# BSD 2-Clause License
#
# Copyright (c) 2020 Ankan Pramanick
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
