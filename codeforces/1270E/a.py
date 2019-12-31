# https://codeforces.com/contest/1270/problem/E
# https://codeforces.com/contest/1270/submission/68006641
# https://github.com/miloszlakomy/competitive/tree/master/codeforces/1270E


def solve(XY):
    while True:
        groups = {}
        for i in range(len(XY)):
            x, y = XY[i]
            groups.setdefault((x % 2, y % 2), []).append(i)

        if len(groups) == 2:
            return next(iter(groups.values()))
        elif len(groups) > 2:
            return (
                groups.get((0, 0), [])
                + groups.get((1, 1), [])
            )

        XY = [(x//2, y//2) for x, y in XY]


n = int(input())
XY = [tuple(int(v) for v in input().split()) for _ in range(n)]

A = solve(XY)
print(len(A))
print(*(i+1 for i in A))
