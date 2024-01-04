#!/usr/bin/env python
from collections import defaultdict
from functools import partial
from itertools import permutations
from pprint import pprint

f = open("9/in.raw", "r")
#f = open("9/sample.raw", "r")
lines = f.read().splitlines()

res=0
origins = set()
distances = {}
for line in lines:
    d, dist = line.split(' = ')
    dist=int(dist)
    origin, destination = d.split(' to ')
    origins.add(origin)
    origins.add(destination)
    distances[(origin,destination)]=dist
    distances[(destination,origin)]=dist

mindist = 9999999999999999999
numdest = len(origins)
maxdist = 0
for c in permutations(origins):
    d = sum((distances[(c[i],c[i+1])] for i in range(numdest-1)))
    mindist=min(mindist,d)
    maxdist=max(maxdist,d)
print(mindist,maxdist)