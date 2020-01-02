/*
https://codeforces.com/contest/1270/problem/G
https://codeforces.com/contest/1270/submission/68061096
https://github.com/miloszlakomy/competitive/tree/master/codeforces/1270G
*/

#include <ios>
#include <iostream>
#include <stack>
#include <unordered_set>
#include <vector>

using Graph = std::vector<std::vector<std::size_t>>;

enum Action {
  SEARCH,
  POP
};

std::unordered_set<std::size_t> find_cycle(const Graph & G) {
  std::unordered_set<std::size_t> seen;

  std::stack<std::pair<std::size_t, Action>> stack;
  std::unordered_set<std::size_t> cycle;

  for (std::size_t i = 0; i < G.size(); ++i) {
    if (seen.find(i) == seen.end()) {
      stack.push({i, Action:SEARCH});
      cycle.clear();

      while (stack.size() > 0) {
        const std::size_t curr_i = stack.top().first;
        const Action action = stack.top().second;
        stack.pop();

        if (Action::POP == action) {
          cycle.erase(curr_i);
        }
        else /* if (Action::SEARCH == action) */ {
          stack.push({curr_i, Action::POP});
          cycle.insert(curr_i);
          seen.insert(curr_i);

          for (const std::size_t next_i : G[curr_i]) {
            if (cycle.find(next_i) != cycle.end()) {
              return cycle;
            }
            if (seen.find(next_i) == seen.end()) {
              stack.push({next_i, Action:SEARCH});
            }
          }
        }
      }
    }
  }

  return {};
}

std::unordered_set<std::size_t> solve(const std::vector<int> & A) {
  const std::size_t n = A.size();

  // G is a directed graph.
  Graph G(n);
  for (std::size_t i = 0; i < n; ++i) {
    int a = A[i];
    int b = i-a;
    G[b].push_back(i);
  }

  return find_cycle(G);
}

int main() {
  std::ios_base::sync_with_stdio(0);
  std::cin.tie(nullptr);

  std::size_t t;

  for (std::cin >> t; t; --t) {
    std::size_t n;
    std::cin >> n;

    std::vector<int> A(n);

    bool short_circuit = false;
    for (std::size_t i = 0; i < n; ++i) {
      int a;
      std::cin >> a;

      if (0 == a) {
        if (!short_circuit) {
          std::cout << 1 << std::endl
              << i+1 << std::endl;
          short_circuit = true;
        }
      }

      A[i] = a;
    }

    if (short_circuit) {
      continue;
    }

    const auto ans = solve(A);
    std::cout << ans.size() << std::endl;
    for (const auto a : ans) {
      std::cout << a+1 << " ";
    }
    std::cout << std::endl;
  }

  return 0;
}
