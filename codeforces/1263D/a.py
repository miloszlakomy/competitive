# https://codeforces.com/problemset/problem/1263/D
# https://codeforces.com/contest/1263/submission/68476829
# https://github.com/miloszlakomy/competitive/tree/master/codeforces/1263D


class FindUnion:
    def __init__(self):
        self._sets = {}  # Maps elements to parents.
        self._count = 0

    def makeset(self, x):
        if x not in self._sets:
            self._sets[x] = x
            self._count += 1

    def find(self, x):
        parent = self._sets[x]

        if self._sets[parent] == parent:
            return parent

        self._sets[x] = self._sets[parent]
        _ = self.find(x)
        return self.find(parent)

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)

        if x_root != y_root:
            self._sets[x_root] = y_root
            self._count -= 1

    def getcount(self):
        return self._count


def solve(F):
    FU = FindUnion()

    for f in F:
        letters = list(f)
        for a in letters:
            FU.makeset(a)
        for i in range(len(letters)):
            a = letters[i]
            for j in range(i+1, len(letters)):
                b = letters[j]
                FU.union(a, b)

    return FU.getcount()


n = int(input())
F = {frozenset(input()) for _ in range(n)}

print(solve(F))
