import re
import sys


puzzle_input = sys.stdin.read()

match_groups = re.findall(
    r"(?:"
        r"(mul)\((\d+),(\d+)\)"
        r"|"
        r"(do)\(\)"
        r"|"
        r"(don't)\(\)"
    r")",
    puzzle_input,
)

result = 0
on = True
for mul, multiplier, multiplicand, do, dont in match_groups:
    if mul and on:
        result += int(multiplier) * int(multiplicand)
    elif do:
        on = True
    elif dont:
        on = False

print(result)

