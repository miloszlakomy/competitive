// https://codeforces.com/problemset/problem/1809/B
// https://codeforces.com/contest/1809/submission/199794299
// https://github.com/miloszlakomy/competitive/tree/master/codeforces/1809B
// https://ideone.com/CmV96I

#include <iostream>
#include <cmath>


template<typename T>
T ceilsqrt(T n) {
  T ret = std::sqrt(n);

  while (ret * ret < n) {
    ret++;
  }

  return ret;
}


void solve_case() {
  long long n;  // Number of chips
  std::cin >> n;

  long long ans = ceilsqrt(n) - 1;

  std::cout << ans << std::endl;
}


void solve_problem() {
  std::size_t t;  // Number of test cases

  for (std::cin >> t; t > 0; t--) {
    solve_case();
  }
}


int main() {
  solve_problem();
  return 0;
}
