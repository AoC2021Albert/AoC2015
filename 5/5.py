#!/usr/bin/env python
from collections import defaultdict
f = open("5/in.raw", "r")
# f = open("5/sample.raw", "r")
lines = f.read().splitlines()

res=0
for line in lines:
  ok = True
  ok = ok and len([c for c in line if c in "aeiou"])>=3
  ok = ok and any([line[i]==line[i+1] for i in range(len(line)-1)])
  ok = ok and line.find('ab') == -1
  ok = ok and line.find('cd') == -1
  ok = ok and line.find('pq') == -1
  ok = ok and line.find('xy') == -1
  if ok:
    res+=1
print(res)

#part 2
res=0
for line in lines:
  ok = True
  ok = ok and any([line[i]==line[i+2] for i in range(len(line)-2)])
  ok = ok and any([line[i]==line[j] and line[i+1]==line[j+1] 
                   for i in range(len(line)-3)
                   for j in range(i+2,len(line)-1)])
  if ok:
    res+=1
print(res)

