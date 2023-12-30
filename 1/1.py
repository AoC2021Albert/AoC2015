#!/usr/bin/env python
from collections import defaultdict
from pprint import pprint
from functools import reduce
from operator import mul
import re
import math

f = open("1/in.raw", "r")
lines = f.read().splitlines()

floor = 0
for i,c in enumerate(lines[0]):
  if floor == -1:
    print(i)
    exit()
  floor = floor + (1 if c=="(" else -1)


