#!/usr/bin/env python

import logging
import pdb
import sys


from basesolver import BaseSolver

class BruteForceBestSolver(BaseSolver):
    """
    Brute force iterates through all possible combinations, returning the
    best one (or more accurately, one of the best ones)
    """


    def solve(self):
        origin = self.current
        seq = [origin]
        self.travelled, self.sequence = self.solve_from_point(seq, 0)

    def solve_from_point(self, current_sequence, current_distance):
        # This seems a bit messy...
        best_remaining_distance = sys.float_info.max
        best_remaining_sequence = None
        for possible_point_id in range(len(self.pointset)):
            if possible_point_id not in current_sequence:
                # print("From %s will next try point %d" % (current_sequence,
                # #                                          possible_point_id))
                new_sequence = current_sequence[:] # copy
                new_sequence.append(possible_point_id)
                # print("new sequence before=%s" % (new_sequence))
                remaining_distance, remaining_sequence = self.solve_from_point(
                    new_sequence,
                    current_distance + self.pointset.distance(current_sequence[-1],
                                                              possible_point_id))
                # print("new sequence after=%s" % (remaining_sequence))
                if remaining_distance < best_remaining_distance:
                    best_remaining_distance = remaining_distance
                    best_remaining_sequence = remaining_sequence
        if not best_remaining_sequence:
            # We must have reached the end, except for returning to the
            # origin point, so do that now
            origin = current_sequence[0]
            current_sequence.append(origin)
            # print("Terminal point found, complete sequence is %s" % (current_sequence))
            return (current_distance + self.pointset.distance(current_sequence[-2],
                                                              origin),
                   current_sequence)

        return best_remaining_distance, best_remaining_sequence



def main(num_points, random_seed):
    foo = BruteForceBestSolver(num_points=num_points, seed=random_seed)
    foo.solve()
    foo.render()
    # foo.plot()

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


