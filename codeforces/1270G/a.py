# https://codeforces.com/contest/1270/problem/G
# https://codeforces.com/contest/1270/submission/68061187
# https://github.com/miloszlakomy/competitive/tree/master/codeforces/1270G


def find_cycle(G):
    seen = set()

    for i in range(len(G)):
        if i not in seen:
            stack = [(i, "search")]
            cycle = set()

            while stack:
                curr_i, action = stack.pop()
                if action == "pop":
                    cycle.remove(curr_i)
                else:  # elif action == "search":
                    stack.append((curr_i, "pop"))
                    cycle.add(curr_i)
                    seen.add(curr_i)

                    for next_i in G[curr_i]:
                        if next_i in cycle:
                            return cycle
                        if next_i not in seen:
                            stack.append((next_i, "search"))

    return None


def solve(A):
    n = len(A)

    # G is a directed graph.
    G = [[] for _ in range(n)]
    for i, a in enumerate(A):
        b = i-a
        G[b].append(i)

    return find_cycle(G)


t = int(input())
for _ in range(t):
    n = int(input())
    A = [int(v) for v in input().split()]

    ans = solve(A)
    print(len(ans))
    print(*(i+1 for i in ans))
