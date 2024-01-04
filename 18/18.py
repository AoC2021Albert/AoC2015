#!/usr/bin/env python
from collections import defaultdict
from functools import partial, reduce
from itertools import permutations
f = open("18/in.raw", "r")
# f = open("18/sample.raw", "r")
lines = f.read().splitlines()
W=len(lines[0])
H=len(lines)

map = [[0] * (W+2)] + \
      [[0]+[0 if c=='.' else 1 for c in l]+[0] for l in lines] + \
      [[0] * (W+2)]

surround = ((-1,-1), (-1, 0), (-1, 1),
            ( 0,-1),          ( 0, 1),
            ( 1,-1), ( 1, 0), ( 1, 1))

def next_map(map):
    ret = [[0] * (W+2) for _ in range(H+2)]
    for y in range(1,H+1):
        for x in range(1,W+1):
            alive=sum(map[y+dy][x+dx] for dy, dx in surround )
            if alive==3:
                ret[y][x]=1
            elif alive==2:
                ret[y][x]=map[y][x]
            else:
                ret[y][x]=0
    return(ret)

map[1][1]=1
map[1][-2]=1
map[-2][1]=1
map[-2][-2]=1

for steps in range(100):
    map = next_map(map)
    map[1][1]=1
    map[1][-2]=1
    map[-2][1]=1
    map[-2][-2]=1
print(sum(sum(l) for l in map))
