The solutions in `a.py` and `b.cpp` are almost the same. Despite that, `b.cpp`
is accepted by the Codeforces checker, while `a.py` gets a time limit exceeded
on the seventieth test.

The solution is based on the union-find data structure (See:
https://en.wikipedia.org/wiki/Disjoint-set_data_structure), with near
constant-time operations, both on average and in the worst case. Note that in
these implementations, the time complexity is amortized, which comes with the
use of a hash table in the data structure definition. This can be worked around
by substituting the hash table for a lookup table, but in practice there's no
significant difference in run time.

Hash tables (Python: *set*, *frozenset*, C++: *unordered_set*) are used to uniq
the input data, which is done for each input string *s*:
 - in *O(26) = O(1)* amortized average time,
 - in *O(len(s))* worst-case time,
 
for all input strings individually:
 - in *O(n)* amortized average time,
 - in *O(n max(len(s)))* worst-case time,
 
then for all processed input strings (with letters uniqed):
 - in *O(26 n) = O(n)* amortized average time,
 - in *O(26 n²) = O(n²)* worst-case time,
 
where the size of the alphabet, 26, determines the cost of generating the hash
values.

*FindUnion* methods have the following time complexities (*α* is the inverse
of the rapidly growing Ackermann function, see:
https://en.wikipedia.org/wiki/Ackermann_function):

*.makeset*:
 - *O(1)* amortized average,
 - *O(n)* worst-case,
 
*.find*:
 - *O(α(n))* amortized average,
 - *O(n α(n))* worst-case,
 
*.union*:
 - *O(α(n))* amortized average,
 - *O(n α(n))* worst-case,
 
*.getcount*:
 - *O(1)* thanks to a *._count* field held and updated additionally in the other
 methods.

*solve* has time complexity
*O(26 L) O(FindUnion.makeset) + O(26²) O(FindUnion.union)
= O(L) O(FindUnion.makeset) + O(FindUnion.union)*, which is:
 - *O(L + α(n))* amortized average,
 - *O(n (L + α(n)))* worst-case.

All in all, the complexity of the solution is:
 - *O(n) + O(n) + O(L + α(n)) = O(L + α(n))* amortized average,
 - *O(n max(len(s))) + O(n²) + O(n (L + α(n))) = O(n (L + α(n)))* worst-case.

Note that in practice, the worst-case complexity of hash table operations
is seen very rarely. Also, *α* grows extraordinarily slowly. We can estimate
the time complexity of the solution in practice to be *O(solution) ≈ O(L)*.
