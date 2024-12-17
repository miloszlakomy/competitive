import collections
import sys

import numpy


puzzle_input = numpy.loadtxt(sys.stdin, dtype=int)
right_counter = collections.Counter(puzzle_input[:,1])
print(
    sum(a * right_counter[a] for a in puzzle_input[:,0])
)

