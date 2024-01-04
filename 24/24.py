#!/usr/bin/env python
from collections import defaultdict
from functools import partial, reduce
from itertools import permutations
f = open("24/in.raw", "r")
# f = open("24/sample.raw", "r")
lines = f.read().splitlines()

d=[int(line) for line in reversed(lines)]
TOTAL=sum(d)
GROUP_WEIGHT= TOTAL//4
N_PACKETS = len(d)
for i in range(N_PACKETS):
    min_qe_i = 9999999999999999999999999999999999
    for p in permutations(d,i):
        if sum(p)==GROUP_WEIGHT:
            min_qe_i=min(min_qe_i,reduce((lambda x, y: x * y), p))
    print(i,min_qe_i)
