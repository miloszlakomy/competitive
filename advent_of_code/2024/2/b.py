import sys


def safe(row):
    min_difference = min(abs(a - b) for a, b in zip(row[:-1], row[1:]))
    max_difference = max(abs(a - b) for a, b in zip(row[:-1], row[1:]))
    increasing = all(a < b for a, b in zip(row[:-1], row[1:]))
    decreasing = all(a > b for a, b in zip(row[:-1], row[1:]))

    return (
        min_difference >= 1 and
        max_difference <= 3 and
        (increasing or decreasing)
    )


def safe_with_one_removed(row):
    """safe_with_one_removed

    O(n²). A O(n) solution exists
    """
    for i in range(len(row)):
        if safe(row[:i] + row[i+1:]):
            return True
    return False


puzzle_input = (
    [int(str_cell) for str_cell in row]
    for row in (
        str_row.split() for str_row in sys.stdin
    )
    if row
)

print(
    sum(1 for row in puzzle_input if safe_with_one_removed(row))
)

