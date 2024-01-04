#!/usr/bin/env python
from collections import defaultdict, deque
from functools import partial, reduce
from itertools import permutations, combinations_with_replacement
from pprint import pprint
f = open("15/in.raw", "r")
#f = open("15/sample.raw", "r")
lines = f.read().splitlines()

capacity, durability, flavor, texture, calories = 0, 1, 2, 3, 4

ingredients={}
for line in lines:
    ingredient, properties = line.split(': ')
    ingredients[ingredient] = [int(p.split(' ')[1])
                               for p in properties.split(', ')]
pprint(ingredients)

mx=0
for c in combinations_with_replacement(ingredients.values(),100):
    mul=1
    for prop in range(4):
        sm = sum(p[prop] for p in c)
        sm = max(0,sm)
        mul = mul*sm
    mx = max(mul,mx)
print(mx)


mx=0
for c in combinations_with_replacement(ingredients.values(),100):
    mul=1
    if sum(p[calories] for p in c) == 500:
        for prop in range(4):
            sm = sum(p[prop] for p in c)
            sm = max(0,sm)
            mul = mul*sm
        mx = max(mul,mx)
print(mx)
