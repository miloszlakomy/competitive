import sys

import numpy


puzzle_input = numpy.loadtxt(sys.stdin, dtype=int)
puzzle_input[:,0].sort()
puzzle_input[:,1].sort()
print(
    sum(abs(a - b) for a, b in puzzle_input)
)
