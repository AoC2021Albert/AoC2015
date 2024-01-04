#!/usr/bin/env python
from collections import defaultdict
from functools import partial, reduce
from itertools import permutations
import re
f = open("14/in.raw", "r")
#f = open("14/sample.raw", "r")
lines = f.read().splitlines()

SPEED, RUNT, RESTT = 0,1,2

reindeer = []
for line in lines:
    r=re.match(r'(.*) can fly (\d*) km/s for (\d*) seconds, but then must rest for (\d*) seconds.', line)
    print(list(r.groups()))
    reindeer.append(tuple(int(r.group(i)) for i in range(2,5)))

points=[0]*len(reindeer)
for t in range(1,2503):
    positions=[0]*len(reindeer)
    top_reindeers = []
    max_pos = 0
    for i, r in enumerate(reindeer):
        positions.append(t//(r[RUNT]+r[RESTT])*(r[SPEED]*r[RUNT]) +
                        min(t%(r[RUNT]+r[RESTT]),r[RUNT])*r[SPEED])
        if positions[-1]>max_pos:
            top_reindeers = [i]
            max_pos = positions[-1]
        elif positions[-1]==max_pos:
            top_reindeers.append(i)
            max_pos = positions[-1]
    for i in top_reindeers:
        points[i]+=1
print(max(points))




