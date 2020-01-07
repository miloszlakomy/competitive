# https://codeforces.com/contest/1270/problem/A
# https://codeforces.com/contest/1270/submission/68348079
# https://github.com/miloszlakomy/competitive/tree/master/codeforces/1270A


t = int(input())

for _ in range(t):
    _ = input()  # n, k_1, k_2
    A = [int(x) for x in input().split()]
    B = [int(x) for x in input().split()]

    if max(A) > max(B):
        print("YES")
    else:
        print("NO")
