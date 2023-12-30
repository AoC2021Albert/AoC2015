#!/usr/bin/env python
from collections import defaultdict
from pprint import pprint
from functools import reduce
from operator import mul
import re
import math

f = open("2/in.raw", "r")
#f = open("2/sample.raw", "r")
lines = f.read().splitlines()

totalarea = 0
totalribbon = 0
for line in lines:
  dim=list(map(int,line.split('x')))
  area = 0
  minarea = 999999999999999999999999999999
  for i in range(len(dim)):
    for j in range(i+1,len(dim)):
      newarea = dim[i]*dim[j]
      area += newarea
      minarea = min(minarea, newarea)
  totalribbon += sum(sorted(dim)[:2])*2
  totalribbon += dim[0]*dim[1]*dim[2]
  print(totalribbon)
  area = area * 2 + minarea
  totalarea += area
print(totalarea)
print(totalribbon)
