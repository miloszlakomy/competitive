The solution in `a.cpp` has amortized time complexity
*O(t len(p)(len(h)-len(p)))*.

The solution in `b.py` has amortized time complexity
*O(t len(h))*.

The solution in `c.go` has better (not amortized) time complexity
*O(t len(h))*.
It also runs each test case in a separate goroutine,
distributing the work across CPU cores.
