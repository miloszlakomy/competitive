# https://codeforces.com/contest/1270/problem/C
# https://codeforces.com/contest/1270/submission/68102390
# https://github.com/miloszlakomy/competitive/tree/master/codeforces/1270C


import functools


def solve(A):
    xored = functools.reduce(lambda a, b: a ^ b, A, 0)
    summed = sum(A)

    if summed == 0:
        return []

    if summed == 1:
        return [3]

    second = 1
    while second & (summed+xored) == 0:
        second <<= 1
    third = (summed+xored) ^ second

    return [xored, second, third]


t = int(input())

for _ in range(t):
    _ = input()  # n
    A = [int(x) for x in input().split()]

    ans = solve(A)
    print(len(ans))
    print(*ans)
