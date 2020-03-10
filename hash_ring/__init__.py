# -*- coding: utf-8 -*-
import sys

if int(sys.version_info.major) >= 3:
    from .hash_ring import HashRing
else:
    from hash_ring import HashRing
