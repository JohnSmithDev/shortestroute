#!/usr/bin/env python


import pdb
import random

from point import Point

class Pointset(object):
    """
    Container for a set/list of points.
    """

    def __init__(self, num_points=None, min=None, max=None, seed=None, pointset=None):
        """
        Either specify a number of points to create a random set from (with
        min, max and seed as ways of controlling the randomness), or pass
        through a previously created pointset.
        """
        if pointset:
            self._points = pointset
        elif num_points:
            if not min:
                min = Point(0, 0)
            if not max:
                max = Point(100, 100)
            if min.x > max.x or min.y > max.y:
                raise ValueError("Illogical min/max for point ranges: %s / %s" %
                                 (min, max))
            if seed:
                random.seed(seed)
            self._points = [Point(random.randint(min.x, max.x), random.randint(min.y, max.y))
                            for _ in range(num_points)]
            # TOOD: avoid having the same point occur twice
        else:
            raise ValueError("Must specify either a number of points, or a pointset")

        self._sorted_distance_cache = {}
        self._points_distance_cache = {}

    @property
    def points(self):
        return self._points

    def distance(self, idx1, idx2):
        # The memoization here gives moderate return e.g.
        # 13 minutes vs 17 minutes for 12 point search
        key = (min(idx1, idx2), max(idx1, idx2))
        try:
            return self._points_distance_cache[key]
        except KeyError:
            d =  self[idx1].distance_from(self[idx2])
            self._points_distance_cache[key] = d
            return d

    def distances_from(self, idx):
        return [(self[idx].distance_from(self[other_idx]), other_idx)
                for other_idx in range(len(self)) if other_idx != idx]

    def sorted_distances_from(self, idx):
        # TODO (maybe): memoize this via a decorator instead?
        try:
            return self._sorted_distance_cache[idx]
        except KeyError:
            self._sorted_distance_cache[idx] = sorted(self.distances_from(idx))
            return self._sorted_distance_cache[idx]


    def __getitem__(self, idx):
        return self.points[idx]

    def __len__(self):
        return len(self.points)

    def __repr__(self):
        return "Set of %d points" % (len(self))


