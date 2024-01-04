#!/usr/bin/env python
from collections import defaultdict, deque
from functools import partial, reduce
from itertools import permutations
f = open("19/in.raw", "r")
#f = open("19/sample2.raw", "r")
#f = open("19/sample.raw", "r")
lines = f.read().splitlines()

def find_all_substrings(string, sub):
    start = 0
    while True:
        start = string.find(sub, start)
        if start == -1: return
        yield start
        start += 1

formula=lines[-1]
options = set()
transforms=defaultdict(dict)
desired_goals=set()
for line in lines[:-2]:
    src, dst = line.split(' => ')
    for p in find_all_substrings(formula,src):
        options.add(formula[:p]+dst+formula[p+len(src):])
    assert dst not in transforms
    if src=='e':
        desired_goals.add(dst)
    else:
        transforms[dst]=src
print(len(options))


attempts = set([formula])
steps=0
while len(attempts)>0:
    steps+=1
    new_attempts = set()
    for attempt in attempts:
        for dst,src in transforms.items():
            for p in find_all_substrings(attempt,dst):
                new_attempt = attempt[:p]+src+attempt[p+len(dst):]
                if new_attempt in desired_goals:
                    print(new_attempt)
                    print(steps+1)
                    exit()
                new_attempts.add(new_attempt)
    print(steps,len(new_attempts))
    attempts = sorted(new_attempts, key=len)[:1]
    print(attempts[0])
print(steps)