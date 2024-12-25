import collections
import sys
from typing import Any

import algutils.char_array

from nptyping import Int, NDArray, Shape
from nptyping.typing_ import Str
import numpy as np


Char = Str
NDArrayChar = NDArray[Any, Char]
Vector2D = NDArray[Shape["1, 2"], Int]
TupleVector2D = tuple[int, int]


def are_coords_in_map(puzzle_map: NDArrayChar, coords: Vector2D) -> bool:
    for coord in coords:
        if coord < 0:
            return False

    try:
        _ = puzzle_map[*coords]
    except IndexError as e:
        if algutils.char_array.OutOfCharArrayIndexError.matches(e):
            return False
        raise

    return True


def inplace_mark_antinodes(
    puzzle_map: NDArrayChar,
    frequency_char_to_antennas_coords: collections.defaultdict[
        Char, set[TupleVector2D]
    ],
):
    for frequency_antennas_coords in frequency_char_to_antennas_coords.values():
        for coords_a in frequency_antennas_coords:
            np_coords_a = np.array(coords_a)
            for coords_b in frequency_antennas_coords:
                if coords_a == coords_b:
                    continue

                np_coords_b = np.array(coords_b)

                np_antinode_coords = np_coords_a + (np_coords_a - np_coords_b)
                if not are_coords_in_map(
                    puzzle_map=puzzle_map,
                    coords=np_antinode_coords,
                ):
                    continue

                puzzle_map[*np_antinode_coords] = "#"


def find_frequency_char_to_antennas_coords(
    puzzle_map: NDArrayChar,
    antennas_coords: set[TupleVector2D],
) -> collections.defaultdict[Char, set[TupleVector2D]]:
    frequency_char_to_antennas_coords: collections.defaultdict[Char, set[TupleVector2D]]
    frequency_char_to_antennas_coords = collections.defaultdict(set)

    for coords in antennas_coords:
        frequency_char_to_antennas_coords[puzzle_map[*coords]].add(coords)

    return frequency_char_to_antennas_coords


def find_antennas_coords(puzzle_map: NDArrayChar) -> set[TupleVector2D]:
    antennas_coords: set[TupleVector2D] = set()

    for y, row in enumerate(puzzle_map):
        for x, _ in enumerate(row):
            coords = (y, x)
            if puzzle_map[*coords] != ".":
                antennas_coords.add(coords)

    return antennas_coords


def main() -> None:
    puzzle_map = algutils.char_array.load_char_array(sys.stdin)
    algutils.char_array.print_char_array(puzzle_map, prefix="puzzle_map=")

    antennas_coords = find_antennas_coords(puzzle_map)
    frequency_char_to_antennas_coords = find_frequency_char_to_antennas_coords(
        puzzle_map,
        antennas_coords,
    )
    inplace_mark_antinodes(puzzle_map, frequency_char_to_antennas_coords)
    number_of_antinodes = np.count_nonzero(puzzle_map == "#")

    print()
    algutils.char_array.print_char_array(puzzle_map, prefix="puzzle_map=")
    print()
    print(f"number_of_antinodes={number_of_antinodes}")


if __name__ == "__main__":
    main()
