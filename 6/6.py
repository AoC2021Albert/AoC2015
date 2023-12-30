#!/usr/bin/env python
from collections import defaultdict
f = open("6/in.raw", "r")
# f = open("6/sample.raw", "r")
lines = f.read().splitlines()

res=0
lights=[[False]*1000 for _ in range(1000)]
for line in lines:
  if line[:5] == 'turn':
    line = line[6:]

