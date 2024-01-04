#!/usr/bin/env python
from collections import defaultdict
from functools import partial, reduce
from itertools import permutations
f = open("17/in.raw", "r")
# f = open("17/sample.raw", "r")
lines = f.read().splitlines()

b=[int(line) for line in lines]

def get_comb(bs,q,sol):
    if len(sol)>4:
        return(0)
    if len(sol) == 4:
        if q == 0:
            return(1)
        else:
            return(0)
    ret=0
    nbs=bs[:]
    for b in bs:
        nbs.remove(b)
        ret+=get_comb(nbs,q-b,sol+[b])
    return(ret)

print(get_comb(b,150,[]))
