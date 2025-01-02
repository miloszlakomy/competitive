from collections.abc import Callable, Generator
import sys

from nptyping import Int, NDArray, Shape
import numpy as np

import algutils.char_array
from algutils.char_array import CharArray
from algutils.color_print import cprint
import algutils.directed_graph
import algutils.utils


Vector2D = NDArray[Shape["1, 2"], Int]
EdgeVectors = list[tuple[Vector2D, Vector2D]]


DIRECTION_TO_ARROW_CHAR = {(0, +1): "→", (-1, 0): "↑", (0, -1): "←", (+1, 0): "↓"}


def all_coordinates(area_map: CharArray) -> Generator[Vector2D]:
    return (np.array(tuple_coords) for tuple_coords in np.ndindex(area_map.shape))


def map_and_edges_to_map_with_arrows(
    area_map: CharArray, edges: EdgeVectors
) -> CharArray:
    h = len(area_map)  # Height
    w = len(area_map[0])  # Width

    map_with_arrows = np.full(shape=(h * 2 - 1, w * 2 - 1), fill_value=" ", dtype=str)
    map_with_arrows[::2, ::2] = area_map

    average: Callable[[Vector2D, Vector2D], Vector2D]
    average = lambda v, w: (v + w) // 2  # pylint: disable=unnecessary-lambda-assignment
    for sc, ec in edges:  # Start, end coordinates
        dc = ec - sc  # Delta coordinates
        map_with_arrows[*average(2 * sc, 2 * ec)] = DIRECTION_TO_ARROW_CHAR[tuple(dc)]

    return map_with_arrows


def detect_edges(area_map: CharArray) -> EdgeVectors:
    neighbors = [np.array([dy, dx]) for dy, dx in DIRECTION_TO_ARROW_CHAR]  # →↑←↓
    edges: EdgeVectors = []

    for y, x in np.ndindex(area_map.shape):
        sh = area_map[y, x]  # String height
        c = np.array([y, x])  # Coordinates
        for dc in neighbors:  # Delta coordinates
            nc = c + dc  # Neighbor coordinates
            h = int(sh)  # Height
            try:
                nh = int(area_map[*nc])
            except IndexError as e:
                if algutils.char_array.OutOfCharArrayIndexError.matches(e):
                    continue
                raise
            if nh == h - 1:
                edges.append((c, nc))

    return edges


def main() -> None:
    area_map = algutils.char_array.load_char_array(sys.stdin)
    area_map_edges = detect_edges(area_map)

    map_with_arrows = map_and_edges_to_map_with_arrows(area_map, area_map_edges)
    map_with_arrows_pretty_string = algutils.char_array.char_array_to_pretty_string(
        map_with_arrows
    )
    print()
    cprint(map_with_arrows_pretty_string)

    directed_graph = algutils.directed_graph.DirectedGraph(
        node_ids=all_coordinates(area_map),
        edges_ids=area_map_edges,
    )
    # print()
    # cprint(directed_graph)

    nines_coords = [
        coords for coords in all_coordinates(area_map) if area_map[*coords] == "9"
    ]
    # print()
    # cprint(nines_coords)

    zeros_coords = [
        coords for coords in all_coordinates(area_map) if area_map[*coords] == "0"
    ]
    # print()
    # cprint(zeros_coords)

    # for nine_coords in nines_coords:
    #     for zero_coords in zeros_coords:
    #         downhill_trails = directed_graph.find_paths(nine_coords, zero_coords)

    #         print()
    #         print()
    #         cprint(f"{nine_coords} -> {zero_coords}")

    #         for trail in downhill_trails:
    #             print()
    #             print()
    #             edges = zip(trail, trail[1:])
    #             trail_map_with_arrows = map_and_edges_to_map_with_arrows(
    #                 area_map, edges
    #             )
    #             trail_map_with_arrows_pretty_string = (
    #                 algutils.char_array.char_array_to_pretty_string(
    #                     trail_map_with_arrows
    #                 )
    #             )
    #             cprint(trail_map_with_arrows_pretty_string)
    # print()

    ratings_sum = 0
    for nine_coords in nines_coords:
        for zero_coords in zeros_coords:
            ratings_sum += algutils.utils.iterable_length(
                directed_graph.find_paths(nine_coords, zero_coords)
            )

    print()
    cprint(ratings_sum)


if __name__ == "__main__":
    main()
