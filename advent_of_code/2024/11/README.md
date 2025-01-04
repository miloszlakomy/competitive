```
$ PYTHONPATH=~/github.com/miloszlakomy/ \
    time python3 ab.py --number-of-steps=25 < ab.in

result_number_of_pebbles=220999
        0.21 real         0.18 user         0.02 sys
```
```
$ PYTHONPATH=~/github.com/miloszlakomy/ \
    time python3 ab.py --number-of-steps=75 < ab.in

result_number_of_pebbles=261936432123724
        5.14 real         4.87 user         0.26 sys
```
```
$ DEBUG=vv PYTHONPATH=~/github.com/miloszlakomy/ \
    time python3 ab.py --number-of-steps=1 < ab_test_1.in

number_of_steps=1
pebbles=[0, 1, 10, 99, 999]
result_pebble_counts=Counter({1: 2, 9: 2, 2024: 1, 0: 1, 2021976: 1})
result_number_of_pebbles=7
        0.19 real         0.16 user         0.02 sys
```
```
$ for number_of_steps in 1 2 3 4 5 6 25; do \
    DEBUG=vv PYTHONPATH=~/github.com/miloszlakomy/ \
        time python3 ab.py --number-of-steps="${number_of_steps}" < ab_test_2.in
done

number_of_steps=1
pebbles=[125, 17]
result_pebble_counts=Counter({253000: 1, 1: 1, 7: 1})
result_number_of_pebbles=3
        0.19 real         0.16 user         0.02 sys

number_of_steps=2
pebbles=[125, 17]
result_pebble_counts=Counter({253: 1, 0: 1, 2024: 1, 14168: 1})
result_number_of_pebbles=4
        0.18 real         0.15 user         0.02 sys

number_of_steps=3
pebbles=[125, 17]
result_pebble_counts=Counter({512072: 1, 1: 1, 20: 1, 24: 1, 28676032: 1})
result_number_of_pebbles=5
        0.17 real         0.14 user         0.02 sys

number_of_steps=4
pebbles=[125, 17]
result_pebble_counts=Counter({2: 2, 512: 1, 72: 1, 2024: 1, 0: 1, 4: 1, 2867: 1, 6032: 1})
result_number_of_pebbles=9
        0.17 real         0.15 user         0.02 sys

number_of_steps=5
pebbles=[125, 17]
result_pebble_counts=Counter({4048: 2, 1036288: 1, 7: 1, 2: 1, 20: 1, 24: 1, 1: 1, 8096: 1, 28: 1, 67: 1, 60: 1, 32: 1})
result_number_of_pebbles=13
        0.17 real         0.14 user         0.02 sys

number_of_steps=6
pebbles=[125, 17]
result_pebble_counts=Counter({2: 4, 0: 2, 40: 2, 48: 2, 6: 2, 2097446912: 1, 14168: 1, 4048: 1, 4: 1, 2024: 1, 80: 1, 96: 1, 8: 1, 7: 1, 3: 1})
result_number_of_pebbles=22
        0.18 real         0.15 user         0.02 sys

number_of_steps=25
pebbles=[125, 17]
result_pebble_counts=Counter({4: 3204, 8: 3146, 0: 2952, 2: 2862, 6: 2571, 8096: 2204, 1: 2138, 4048: 2099, 16192: 2098, 12144: 1737, 7: 1483, 9: 1448, 24: 1389, 80: 1332, 2024: 1224, 96: 1196, 48: 1193, 32772608: 1137, 20: 1065, 40: 1057, 14168: 1040, 3277: 926, 2608: 926, 18216: 918, 24579456: 853, 32: 849, 2457: 802, 9456: 802, 3: 727, 5: 606, 77: 559, 26: 559, 60: 524, 6072: 517, 36869184: 496, 28676032: 481, 2867: 465, 6032: 465, 10120: 464, 57: 460, 94: 460, 56: 460, 3686: 446, 9184: 446, 28: 426, 67: 290, 36: 245, 86: 245, 91: 245, 84: 245, 72: 234, 2048: 212, 2880: 212, 20482880: 172})
result_number_of_pebbles=55312
        0.18 real         0.16 user         0.02 sys
```
