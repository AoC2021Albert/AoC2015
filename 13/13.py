#!/usr/bin/env python
from collections import defaultdict
from functools import partial
from itertools import permutations
from pprint import pprint

f = open("13/in.raw", "r")
#f = open("13/sample.raw", "r")
lines = f.read().splitlines()

res=0
origins = set()
distances = {}
for line in lines:
    origin, rest = line.split(' would ')
    d, destination = rest.split(' happiness units by sitting next to ')
    destination=destination[:-1] # Final period out
    sign, value = d.split(' ')
    dist=int(value)* (1 if sign=="gain" else -1)
    origins.add(origin)
    origins.add(destination)
    distances[(origin,destination)]=dist

mindist = 9999999999999999999
numdest = len(origins)
maxdist = 0
for c in permutations(origins):
    d = sum((distances[(c[i],c[(i+1)%numdest])] +
             distances[(c[i],c[(i-1)%numdest])]
             for i in range(numdest)))
    mindist=min(mindist,d)
    maxdist=max(maxdist,d)
print(mindist,maxdist)

# part 2
for guest in origins:
    distances[('me',guest)]=0
    distances[(guest,'me')]=0
origins.add('me')

mindist = 9999999999999999999
numdest = len(origins)
maxdist = 0
for c in permutations(origins):
    d = sum((distances[(c[i],c[(i+1)%numdest])] +
             distances[(c[i],c[(i-1)%numdest])]
             for i in range(numdest)))
    mindist=min(mindist,d)
    maxdist=max(maxdist,d)
print(mindist,maxdist)