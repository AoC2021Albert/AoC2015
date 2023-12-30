#!/usr/bin/env python
from collections import defaultdict
f = open("3/in.raw", "r")
# f = open("3/sample.raw", "r")
lines = f.read().splitlines()
DIR = '>v<^'
next_step = [(1), (1j), (-1), (-1j)]
p=0
visited=defaultdict(int)
visited[p]=1
for c in lines[0]:
  p+=next_step[DIR.index(c)]
  visited[p]+=1
print(len(visited))

# Part 2
i=0
santa=0
robosanta=0
visited=set([0])
while i<len(lines[0]):
  santa += next_step[DIR.index(lines[0][i])]
  robosanta += next_step[DIR.index(lines[0][i+1])]
  visited.add(santa)
  visited.add(robosanta)
  i+=2
print(len(visited))
