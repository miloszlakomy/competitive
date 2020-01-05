# https://codeforces.com/contest/1270/problem/B
# https://codeforces.com/contest/1270/submission/68220722
# https://github.com/miloszlakomy/competitive/tree/master/codeforces/1270B


def solve(A):
    for cand in range(len(A)-1):
        if abs(A[cand] - A[cand+1]) >= 2:
            return cand, cand+2
    return None


t = int(input())

for _ in range(t):
    _ = input()  # n
    A = [int(x) for x in input().split()]

    ans = solve(A)
    if ans is None:
        print("NO")
    else:
        print("YES")
        start, end = ans
        print(start+1, end)
