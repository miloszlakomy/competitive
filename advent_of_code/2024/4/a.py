import itertools
import re
import sys
import warnings

import numpy


def rows(numpy_array):
    for row in numpy_array:
        yield "".join(row)


def columns(numpy_array):
    for column in numpy_array.transpose():
        yield "".join(column)


def slash_diagonals(numpy_array):
    num_rows, num_columns = numpy_array.shape
    for offset in range(-num_rows + 1, num_columns):
        yield "".join(numpy.diagonal(numpy_array, offset=offset))


def backslash_diagonals(numpy_array):
    num_rows, num_columns = numpy_array.shape
    for offset in range(-num_rows + 1, num_columns):
        yield "".join(numpy.diagonal(numpy_array[::-1], offset=offset))


warnings.filterwarnings(
    action="ignore",
    message=r"Input line \d+ contained no data.*NumPy.*",
)
puzzle_input = numpy.loadtxt(sys.stdin, dtype=str)
puzzle_input = puzzle_input.view("U1").reshape(puzzle_input.size, -1)

needle = r"XMAS"

print(
    sum(
        len(re.findall(needle, haystack))
        + len(re.findall(needle[::-1], haystack))
        for haystack in itertools.chain(
            rows(puzzle_input),
            columns(puzzle_input),
            slash_diagonals(puzzle_input),
            backslash_diagonals(puzzle_input),
        )
    )
)

