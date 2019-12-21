# https://codeforces.com/contest/1278/problem/A
# https://codeforces.com/contest/1278/submission/67379618
# https://github.com/miloszlakomy/competitive/tree/master/codeforces/1278A


import collections


def solve(p, h):
    pms = collections.Counter(p)
    hms = collections.Counter(h[:len(p)])

    if pms == hms:
        return "YES"

    for i in range(len(h) - len(p)):
        hms[h[i]] -= 1
        if hms[h[i]] == 0:
            del hms[h[i]]

        hms[h[i + len(p)]] += 1

        if pms == hms:
            return "YES"

    return "NO"


t = int(input())

for _ in range(t):
    p = input()
    h = input()

    print(solve(p, h))
