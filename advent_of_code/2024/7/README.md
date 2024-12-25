https://adventofcode.com/2024/day/7

```Bash
$ /usr/bin/time python3 a.py < ab_test.in
3749
        0.03 real         0.02 user         0.00 sys
```
```Bash
$ /usr/bin/time python3 b.py < ab_test.in
11387
        0.21 real         0.88 user         0.22 sys
```
```Bash
$ /usr/bin/time python3 a.py < ab.in > /dev/null
        0.27 real         0.26 user         0.00 sys
```
```Bash
$ /usr/bin/time python3 b.py < ab.in > /dev/null
        2.65 real        26.85 user         0.47 sys
```
