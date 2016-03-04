#!/usr/bin/env python
"""

"""

import logging
import sys
import unittest

import simplejson as json

from ..point import Point

class TestPoint(unittest.TestCase):

    def testDistance(self):
        a = Point(0,0)
        b = Point(3,4)
        self.assertEqual(5, a.distance_from(b))
        self.assertEqual(5, b.distance_from(a))
        self.assertEqual(5, a - b)
        self.assertEqual(5, b - a)

    def testNoDistance(self):
        a = Point(0,0)
        b = Point(0,0)
        self.assertEqual(0, a.distance_from(b))
        self.assertEqual(0, b.distance_from(a))
        self.assertEqual(0, a - b)
        self.assertEqual(0, b - a)


