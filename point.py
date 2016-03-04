#!/usr/bin/env python
"""

"""

from __future__ import division

import math


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_from(self, other):
        return math.sqrt(pow(other.x - self.x, 2) + pow(other.y - self.y, 2))

    def __sub__(self, other):
        return self.distance_from(other)

    def astuple(self):
        """Useful for feeding into matplotlib"""
        return (self.x, self.y)

    def __repr__(self):
        return "Point at (%s,%s)" % (self.x, self.y)


