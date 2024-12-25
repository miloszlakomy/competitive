import concurrent.futures
import itertools
import sys
from typing import Callable, Iterator, Optional


Operands = list[int]
Operator = Callable[[int, int], int]
Operators = list[Operator]
PuzzleCase = tuple[int, Operands]
PuzzleCases = list[PuzzleCase]


def calculate_left_to_right(
    operators: Operators, operands: Operands, limit: int
) -> Optional[int]:
    result = operands[0]
    for operator, operand in zip(operators, operands[1:]):
        if result > limit:
            return None
        result = operator(result, operand)
    return result


def plus(a: int, b: int) -> int:
    return a + b


def times(a: int, b: int) -> int:
    return a * b


def concatenate(a: int, b: int) -> int:
    return int(f"{a}{b}")


def result_if_matching_operators_can_be_guessed_else_zero(
    puzzle_case: PuzzleCase,
) -> int:
    result, operands = puzzle_case

    operators_guesses: Iterator[Operators] = (
        list(operators)
        for operators in itertools.product(
            [plus, times, concatenate],
            repeat=len(operands) - 1,
        )
    )

    for operators in operators_guesses:
        if result == calculate_left_to_right(operators, operands, limit=result):
            return result
    return 0


def read_puzzle_cases_from_stdin() -> PuzzleCases:
    puzzle_cases: PuzzleCases = []
    for line in sys.stdin.readlines():
        result_str, operands_str = line.split(":")
        result = int(result_str)
        operands_strs = operands_str.strip().split(" ")
        operands = [int(operand_str) for operand_str in operands_strs]
        puzzle_cases.append((result, operands))

    return puzzle_cases


def main() -> None:
    puzzle_cases = read_puzzle_cases_from_stdin()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        matching_results_sum = sum(
            executor.map(
                result_if_matching_operators_can_be_guessed_else_zero,
                puzzle_cases,
            )
        )
    print(matching_results_sum)


if __name__ == "__main__":
    main()
