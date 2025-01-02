from collections.abc import Callable, Generator
import sys

from nptyping import Int, NDArray, Shape
import numpy as np

import algutils.char_array
from algutils.char_array import CharArray
from algutils.color_print import cprint
import algutils.directed_graph
from algutils.utils import debug, vdebug, vvdebug


Vector2D = NDArray[Shape["1, 2"], Int]
EdgeVectors = list[tuple[Vector2D, Vector2D]]


DIRECTION_TO_ARROW_CHAR = {(0, +1): "→", (-1, 0): "↑", (0, -1): "←", (+1, 0): "↓"}


# Debug functions:


def print_all_uphill_trails(
    area_map: CharArray,
    edges: EdgeVectors,
    zeros_coords: list[Vector2D],
    nines_coords: list[Vector2D],
    directed_graph: algutils.directed_graph.DirectedGraph,
) -> None:
    for zero_coords in zeros_coords:
        for nine_coords in nines_coords:
            uphill_trails = directed_graph.find_paths(zero_coords, nine_coords)

            print()
            print()
            cprint(f"{zero_coords} -> {nine_coords}")

            for trail in uphill_trails:
                edges = zip(trail, trail[1:])
                trail_map_with_arrows = map_and_edges_to_map_with_arrows(
                    area_map, edges
                )
                trail_map_with_arrows_pretty_string = (
                    algutils.char_array.char_array_to_pretty_string(
                        trail_map_with_arrows
                    )
                )
                print()
                print()
                cprint(trail_map_with_arrows_pretty_string)
            print()
    print()


def print_map_with_arrows(
    area_map: CharArray, edges: EdgeVectors
) -> None:
    map_with_arrows = map_and_edges_to_map_with_arrows(area_map, edges)

    map_with_arrows_pretty_string = algutils.char_array.char_array_to_pretty_string(
        map_with_arrows
    )
    cprint("", "map_with_arrows_pretty_string=", map_with_arrows_pretty_string, sep="\n\n")


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


# Utility functions:


def all_coordinates(area_map: CharArray) -> Generator[Vector2D]:
    return (np.array(tuple_coords) for tuple_coords in np.ndindex(area_map.shape))


def detect_edges(area_map: CharArray) -> EdgeVectors:
    neighbors = [np.array([dy, dx]) for dy, dx in DIRECTION_TO_ARROW_CHAR]  # →↑←↓
    edges: EdgeVectors = []

    for y, x in np.ndindex(area_map.shape):
        sh = area_map[y, x]  # String height
        c = np.array([y, x])  # Coordinates
        for dc in neighbors:  # Delta coordinates
            nc = c + dc  # Neighbor coordinates
            ncx, ncy = nc
            if ncx < 0 or ncy < 0:
                continue
            h = int(sh)  # Height
            try:
                nh = int(area_map[*nc])
            except IndexError as e:
                if algutils.char_array.OutOfCharArrayIndexError.matches(e):
                    continue
                raise
            if nh == h + 1:
                edges.append((c, nc))

    if debug():
        print_map_with_arrows(area_map, edges)
    if vvdebug():
        cprint("", "edges=", edges, sep="\n")

    return edges


def main() -> None:
    area_map = algutils.char_array.load_char_array(sys.stdin)
    area_map_edges = detect_edges(area_map)

    directed_graph = algutils.directed_graph.DirectedGraph(
        node_ids=all_coordinates(area_map),
        edges_ids=area_map_edges,
    )
    if vdebug():
        cprint("", "directed_graph=", directed_graph, sep="\n")

    zeros_coords = [
        coords for coords in all_coordinates(area_map) if area_map[*coords] == "0"
    ]
    if vdebug():
        cprint("", "zeros_coords=", zeros_coords, sep="\n")

    nines_coords = [
        coords for coords in all_coordinates(area_map) if area_map[*coords] == "9"
    ]
    if vdebug():
        cprint("", "nines_coords=", nines_coords, sep="\n")

    if vvdebug():
        print_all_uphill_trails(
            area_map, area_map_edges, zeros_coords, nines_coords, directed_graph
        )

    score_sum = 0
    if vdebug():
        print()
    for zero_coords in zeros_coords:
        score = 0
        for nine_coords in nines_coords:
            path_exists = directed_graph.path_exists(zero_coords, nine_coords)
            if path_exists:
                score += 1
            if vvdebug():
                cprint(f"{zero_coords} -> {nine_coords}: path_exists={path_exists}")
        score_sum += score
        if vdebug():
            print()
            cprint(f"{zero_coords}: score={score}")
            print()

    print()
    cprint(f"score_sum={score_sum}")
    print()


if __name__ == "__main__":
    main()
