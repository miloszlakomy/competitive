# https://codeforces.com/contest/1739/problem/A
# https://codeforces.com/contest/1739/submission/179613447
# https://github.com/miloszlakomy/competitive/tree/master/codeforces/1739A


t = int(input())

for _ in range(t):
    n, m = [int(x) for x in input().split()]

    if min(n, m) <= 1:
        print("1 1")
    else:
        print("2 2")
