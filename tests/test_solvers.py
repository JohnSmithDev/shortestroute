#!/usr/bin/env python
"""

"""

import unittest

from ..point import Point
from ..pointset import Pointset
from ..nextnearest import NextNearestSolver
from ..bruteforcebest import BruteForceBestSolver

class _BaseTestSolver(unittest.TestCase):

    def testEasyRoute(self):
        ps = Pointset(pointset=[Point(0,0), Point(1, 0),
                                Point(1, 2), Point(0, 4)])
        solver = self.solver_class(pointset=ps)
        solver.solve()
        seq = solver.sequence
        self.assertEqual([0,1,2,3,0], seq)
        self.assertEqual(92, int(solver.travelled * 10)) # 9.2360679775


class TestNextNearestSolver(_BaseTestSolver):
    solver_class = NextNearestSolver


class TestBruteForceBestSolver(_BaseTestSolver):
    solver_class = BruteForceBestSolver

