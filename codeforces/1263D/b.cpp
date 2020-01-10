/*
https://codeforces.com/problemset/problem/1263/D
https://codeforces.com/contest/1263/submission/68476702
https://github.com/miloszlakomy/competitive/tree/master/codeforces/1263D
*/


#include <iostream>
#include <string>
#include <unordered_map>
#include <unordered_set>


class FindUnion {
  std::unordered_map<char, char> sets;  // Maps elements to parents.
  std::size_t count = 0;

public:

  void makeset(const char x) {
    if (!sets.count(x)) {
      sets[x] = x;
      ++count;
    }
  }

  char find(const char x) {
    const char parent = sets[x];
    const char grandparent = sets[parent];

    if (grandparent == parent) {
      return parent;
    }

    sets[x] = grandparent;
    find(x);  // Returned value intentionally ignored.
    return find(parent);
  }

  void unite(const char x, const char y) {
    const char x_root = find(x);
    const char y_root = find(y);

    if (x_root != y_root) {
      sets[x_root] = y_root;
      --count;
    }
  }

  std::size_t getcount() {
    return count;
  }
};


std::size_t solve(
    const std::unordered_set<std::string> & F) {
  FindUnion FU;

  for (const auto & letters : F) {
    for (const char a : letters) {
      FU.makeset(a);
    }

    for (std::size_t i = 0; i < letters.size(); ++i) {
      const char a = letters[i];
      for (std::size_t j = i+1; j < letters.size(); ++j) {
        const char b = letters[j];
        FU.unite(a, b);
      }
    }
  }

  return FU.getcount();
}


int main() {
  std::ios_base::sync_with_stdio(0);
  std::cin.tie(nullptr);

  std::size_t n;
  std::cin >> n;
  std::unordered_set<std::string> F;

  for (std::size_t i = 0; i < n; ++i) {
    std::string s;
    std::cin >> s;
    const std::unordered_set<char> us(s.begin(), s.end());
    F.insert(std::string(us.begin(), us.end()));
  }

  std::cout << solve(F) << std::endl;

  return 0;
}
