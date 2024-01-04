#!/usr/bin/env python
from collections import defaultdict
from functools import partial
f = open("8/in.raw", "r")
#f = open("8/sample.raw", "r")
lines = f.read().splitlines()

res=0
for line in lines:
    res+=2
    tres=line.count(r'"')
    tres+=line.count(chr(92))
    print(tres,line)
    res+=tres
print(res)