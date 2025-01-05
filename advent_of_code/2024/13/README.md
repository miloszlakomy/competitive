```Bash
$ PYTHONPATH=~/github.com/miloszlakomy/ time python3 a.py < ab.in
```
```Python
prizes_cost=32067
        0.51 real         0.43 user         0.07 sys
```

<br />

```Bash
$ PYTHONPATH=~/github.com/miloszlakomy/ time python3 b.py < ab.in
```
```Python
prizes_cost=92871736253789
        0.48 real         0.41 user         0.07 sys
```

<br />

```Bash
$ DEBUG=vv PYTHONPATH=~/github.com/miloszlakomy/ time python3 a.py < ab_test.in
```
```Python
machines_behavior=
[MachineBehavior(a⃗=array([94, 34]), b⃗=array([22, 67]), p⃗=array([8400, 5400])),
 MachineBehavior(a⃗=array([26, 66]), b⃗=array([67, 21]), p⃗=array([12748, 12176])),
 MachineBehavior(a⃗=array([17, 86]), b⃗=array([84, 37]), p⃗=array([7870, 6450])),
 MachineBehavior(a⃗=array([69, 23]), b⃗=array([27, 71]), p⃗=array([18641, 10279]))]

machine_number=0
1°
𝛼=80, 𝛽=40
prize_cost=280

machine_number=1
1°
𝛼=141, 𝛽=135
prize_cost=None

machine_number=2
1°
𝛼=38, 𝛽=86
prize_cost=200

machine_number=3
1°
𝛼=244, 𝛽=65
prize_cost=None

prizes_cost=480
        0.48 real         0.41 user         0.06 sys
```

<br />

```Bash
$ DEBUG=vv PYTHONPATH=~/github.com/miloszlakomy/ time python3 b.py < ab_test.in
```
```Python
machines_behavior=
[MachineBehavior(a⃗=array([94, 34]), b⃗=array([22, 67]), p⃗=array([10000000008400, 10000000005400])),
 MachineBehavior(a⃗=array([26, 66]), b⃗=array([67, 21]), p⃗=array([10000000012748, 10000000012176])),
 MachineBehavior(a⃗=array([17, 86]), b⃗=array([84, 37]), p⃗=array([10000000007870, 10000000006450])),
 MachineBehavior(a⃗=array([69, 23]), b⃗=array([27, 71]), p⃗=array([10000000018641, 10000000010279]))]

machine_number=0
1°
𝛼=81081081161, 𝛽=108108108148
prize_cost=None

machine_number=1
1°
𝛼=118679050709, 𝛽=103199174542
prize_cost=459236326669

machine_number=2
1°
𝛼=71266110727, 𝛽=104624715779
prize_cost=None

machine_number=3
1°
𝛼=102851800151, 𝛽=107526881786
prize_cost=416082282239

prizes_cost=875318608908
        0.49 real         0.42 user         0.07 sys
```
