import re
import sys


puzzle_input = sys.stdin.read()

str_mul_args = re.findall(r"mul\((\d+),(\d+)\)", puzzle_input)
mul_args = ((int(str_a), int(str_b)) for str_a, str_b in str_mul_args)
print(
    sum(a * b for a, b in mul_args)
)

