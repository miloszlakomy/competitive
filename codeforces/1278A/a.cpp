// https://codeforces.com/contest/1278/problem/A
// https://codeforces.com/contest/1278/submission/67289143
// https://github.com/miloszlakomy/competitive/tree/master/codeforces/1278A
// https://ideone.com/3D0Ahi

#include <iostream>
#include <string>
#include <unordered_set>

int main() {
  std::size_t t;
  std::string p, h;

  for (std::cin >> t; t; --t) {
    std::cin >> p;
    std::cin >> h;

    std::unordered_multiset<char> pms(p.begin(), p.end());
    std::string ans = "NO";

    for (std::size_t i = 0;
        i + p.size() <= h.size();
        ++i) {
      std::unordered_multiset<char> hms(
          h.begin() + i,
          h.begin() + i + p.size());

      if (pms == hms) {
        ans = "YES";
        break;
      }
    }

    std::cout << ans << std::endl;
  }

  return 0;
}
