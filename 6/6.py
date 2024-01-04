#!/usr/bin/env python
from collections import defaultdict
f = open("6/in.raw", "r")
# f = open("6/sample.raw", "r")
lines = f.read().splitlines()

res=0
lights=[[False]*1000 for _ in range(1000)]
actions = {
  'on': lambda y, x: True,
  'off': lambda y, x: False,
  'toggle': lambda y, x: not(lights[y][x]),
  }

for line in lines:
  if line[:5] == 'turn ':
    line = line[5:]
  kind, tl, _, br = line.split(' ')
  top, left = tuple(map(int,tl.split(',')))
  bottom, right = tuple(map(int,br.split(',')))
  for y in range(top, bottom+1):
    for x in range(left, right+1):
      lights[y][x]=actions[kind](y,x)

res=0
for lightrow in lights:
  for light in lightrow:
    if light:
      res+=1
print(res)

# Part 2
res=0
lights=[[0]*1000 for _ in range(1000)]
actions = {
  'on': lambda y, x: lights[y][x]+1,
  'off': lambda y, x: 0 if lights[y][x] <= 1 else lights[y][x]-1,
  'toggle': lambda y, x: lights[y][x]+2,
  }

for line in lines:
  if line[:5] == 'turn ':
    line = line[5:]
  kind, tl, _, br = line.split(' ')
  top, left = tuple(map(int,tl.split(',')))
  bottom, right = tuple(map(int,br.split(',')))
  for y in range(top, bottom+1):
    for x in range(left, right+1):
      lights[y][x]=actions[kind](y,x)

res=0
for lightrow in lights:
  for light in lightrow:
    res+=light
print(res)
