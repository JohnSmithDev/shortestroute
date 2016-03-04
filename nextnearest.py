#!/usr/bin/env python

import logging
import sys


from basesolver import BaseSolver

class NextNearestSolver(BaseSolver):
    """
    Fairly naive - but hopefully reasonable - algorithm that always picks the
    nearest unvisited point to the current one.
    """

    def solve(self):
        origin = self.current
        while len(self.sequence) < len(self.pointset)-1:
            self.sequence.append(self.current)
            distance, new_point_id = self.find_nearest_unvisited(self.current)
            self.travelled += distance
            self.current = new_point_id
        self.sequence.append(self.current)
        self.travelled += self.pointset.distance(self.current, origin)
        self.sequence.append(origin)


def main(num_points, random_seed):
    foo = NextNearestSolver(num_points=num_points, seed=random_seed)
    foo.solve()
    foo.render()
    foo.plot()

if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)-15s %(message)s')
    logging.getLogger().setLevel(logging.DEBUG)
    try:
        num_points = int(sys.argv[1])
    except IndexError:
        num_points = None # let something else decide the default
    try:
        random_seed = sys.argv[2]
    except IndexError:
        random_seed = None # let something else decide the default

    main(num_points, random_seed)


