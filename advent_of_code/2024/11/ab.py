from collections import Counter
from functools import cache

import click

from algutils.color_print import cprint
from algutils.utils import debug, vdebug, vvdebug


Pebble = PebbleCount = int
Pebbles = list[Pebble]
PebbleCounts = Counter[Pebble, PebbleCount]


def map_step(pebble: Pebble) -> Pebbles:
    if pebble == 0:
        return [1]
    str_pebble = str(pebble)
    l = len(str_pebble)
    if l % 2 == 0:
        return [
            int(str_pebble[: l // 2]),
            int(str_pebble[l // 2 :]),
        ]
    return [2024 * pebble]


@cache
def single_value_mapreduce(pebble: Pebble, number_of_steps: int) -> PebbleCounts:
    if number_of_steps == 0:
        return Counter([pebble])
    mapped_pebbles = map_step(pebble)
    return sum(
        (
            single_value_mapreduce(pebble, number_of_steps - 1)
            for pebble in mapped_pebbles
        ),
        start=Counter(),
    )


def mapreduce(pebbles: Pebbles, number_of_steps: int) -> PebbleCounts:
    return sum(
        (single_value_mapreduce(pebble, number_of_steps) for pebble in pebbles),
        start=Counter(),
    )


def read_input_from_stdin() -> Pebbles:
    return [int(str_pebble) for str_pebble in input().split()]


@click.command()
@click.option(
    "--number-of-steps", "-n", type=int, required=True, help="Number of blinks"
)
def main(number_of_steps: int) -> None:
    pebbles = read_input_from_stdin()

    if debug():
        cprint(f"pebbles={pebbles}")

    result_pebble_counts = mapreduce(pebbles, number_of_steps)

    if vdebug():
        cprint(f"result_pebble_counts={result_pebble_counts}")

    result_number_of_pebbles = sum(result_pebble_counts.values())

    cprint(f"result_number_of_pebbles={result_number_of_pebbles}")


if __name__ == "__main__":
    main()
