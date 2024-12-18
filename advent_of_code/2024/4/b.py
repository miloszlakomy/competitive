import itertools
import re
import sys
import warnings

import numpy


def needle_matches_haystack(needle, haystack):
    if needle.shape != haystack.shape:
        return False

    return all(
        (
            n == "."
            or n == h
        )
        for n, h in zip(needle.ravel(), haystack.ravel())
    )


warnings.filterwarnings(
    action="ignore",
    message=r"Input line \d+ contained no data.*NumPy.*",
)
puzzle_input = numpy.loadtxt(sys.stdin, dtype=str)
# Convert 1D array of strs to 2D array of characters
puzzle_input = puzzle_input.view("U1").reshape(puzzle_input.size, -1)
puzzle_input_height, puzzle_input_width = puzzle_input.shape

needle_base = numpy.array("M.S\n.A.\nM.S".split("\n"))
needle_base = needle_base.view("U1").reshape(needle_base.size, -1)
needle_height, needle_width = needle_base.shape

needles = {
    needle.tobytes(): needle
    for needle in [
        needle_base,
        needle_base[::-1],
        needle_base[:,::-1],
        needle_base[::-1,::-1],
        needle_base.transpose(),
        needle_base.transpose()[::-1],
        needle_base.transpose()[:,::-1],
        needle_base.transpose()[::-1,::-1],
    ]
}.values()

# O(nm) where n=needle_height * needle_width, m=puzzle_input_height * puzzle_input_width
# An O(n+m) solution exists, generalizing the KMP algorithm
print(
    sum(
        1
        for needle in needles
        for haystack in (
            puzzle_input[y:y + needle_height, x:x + needle_width]
            for y in range(puzzle_input_height - needle_height + 1)
            for x in range(puzzle_input_width - needle_width + 1)
        )
        if needle_matches_haystack(needle, haystack)
    )
)

