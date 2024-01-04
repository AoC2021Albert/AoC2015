#!/usr/bin/env python
from collections import defaultdict
from functools import partial, reduce
from itertools import permutations
f = open("23/in.raw", "r")
# f = open("23/sample.raw", "r")
lines = f.read().splitlines()

def tpl(op, dst, ip, r):
    r[op] *= 3
    return(ip + 1, r)

def hlf(op, dst, ip, r):
            r[op] = r[op] // 2
            return(ip + 1, r)

def inc(op, dst, ip, r):
            r[op] += 1
            return(ip + 1, r)

def jmp(op, dst, ip, r):
            return(ip + int(op), r)

def jie(op, dst, ip, r):
            return(ip + int(dst) if r[op] % 2 == 0 else ip + 1, r)

def jio(op, dst, ip, r):
            return(ip + int(dst) if r[op] == 1 else ip + 1, r)

prg=[]
for n, line in enumerate(lines):
    if line.find(',')!=-1:
        inst, dst = line.split(', ')
    else:
        inst = line
    cmd, op = inst.split(' ')
    prg.append((partial(locals()[cmd],op,dst)))

ip = 0
r = {
    'a' : 1,
    'b' : 0
}
while ip < len(lines):
    ip, r = prg[ip](ip, r)
print(r['b'])