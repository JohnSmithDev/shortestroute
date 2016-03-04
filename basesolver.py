#!/usr/bin/env python

import abc

from matplotlib import pyplot as plt
from matplotlib import path as mpath

from pointset import Pointset

class BaseSolver(object):
    """
    Base class for solving route through a pointset.

    Implement solve() in your concrete class.
    """

    __metaclass__ = abc.ABCMeta

    def __init__(self, pointset=None, num_points=None, seed=None):
        if pointset:
            self.pointset = pointset
        else:
            self.pointset = Pointset(num_points=num_points or 10,
                                     seed=seed)

        self.sequence = []
        self.current = 0
        self.travelled = 0.0

    @abc.abstractmethod
    def solve(self):
        raise NotImplementedError

    def find_nearest_unvisited(self, starting_point_id): # Should this be in base?
        all_options = self.pointset.sorted_distances_from(starting_point_id)

        available_options = [z for z in all_options if z[1] not in self.sequence]
        # Observation: the index of the best available option should be a metric
        # of how optimal our solution is i.e.
        # - if we always pick the first item in all_options, ultimately we'd have
        #   a perfect solution
        # - if we end up picking lots of values from the latter half of all_options,
        #   that might imply we have a suboptimal solution
        # print("Available options from %s are %s" % (starting_point_id, available_options))
        return available_options[0]

    def render(self):
        cumulative_distance = 0.0
        for i, pt in enumerate(self.sequence[:-1]):
            next_pt = self.sequence[i+1]
            this_distance = self.pointset.distance(pt, next_pt)
            cumulative_distance += this_distance
            print("%02d. From %s to %s, distance=%03d, cumulative distance=%04d" %
                  (i, pt, next_pt, int(this_distance), int(cumulative_distance)))
        print("Total distance: %s" % (self.travelled))

    def plot(self):
        # http://matplotlib.org/examples/shapes_and_collections/path_patch_demo.html
        fig, ax = plt.subplots()
        Path = mpath.Path
        path_data = [(Path.MOVETO, self.pointset[0].astuple())]
        for pt_id in self.sequence[1:]:
            path_data.append((Path.LINETO, self.pointset[pt_id].astuple()))
        codes, verts = zip(*path_data)
        path = mpath.Path(verts, codes)
        x, y = zip(*path.vertices)
        line, = ax.plot(x, y, 'go-') # 'go-' = green, circle, solid line
        ax.grid()
        ax.axis('equal')
        plt.show()


    def __repr__(self):
        return "Total distance travelled: %s" % (self.travelled)

