#!/usr/bin/env python
from collections import defaultdict, deque
from functools import partial, reduce
from itertools import permutations
from pprint import pprint
import re
f = open("21/in.raw", "r")
lines = f.read().splitlines()

assets=defaultdict(list)
for line in lines:
    l=re.match(r'.* +([0-9]+) +([0-9]+) +([0-9]+)',line)
    if l:
        assets[kind].append(tuple(list(map(int,(l[1],l[2],l[3])))))
    elif line!="":
        kind, _ = line.split(': ')

f = open("21/adversary.raw", "r")
lines = f.read().splitlines()
boss_hp = int(lines[0].split(': ')[1])
boss_damage = int(lines[1].split(': ')[1])
boss_armor = int(lines[2].split(': ')[1])

# Pick no armor option
assets['Armor'].append((0,0,0))

ringcombinations=set()
assets['Rings'].append((0,0,0))
for i_ring1, ring1 in enumerate(assets['Rings']):
    for i_ring2 in range(i_ring1+1,len(assets['Rings'])):
        ring2=assets['Rings'][i_ring2]
        ringcombinations.add(tuple(ring1[i]+ring2[i] for i in range(3)))

possible_purchases = []
for weapon in sorted(assets['Weapons']):
    for armor in sorted(assets['Armor']):
        for ring in sorted(ringcombinations):
            possible_purchases.append(list(map(sum,zip(weapon,armor,ring))))

def fight(assets):
    my_hp_left=100
    my_damage=assets[1]
    my_armor=assets[2]
    # the global ones loaded before
    boss_hp_left=boss_hp
    boss_decrease = my_damage - boss_armor
    my_decrease = boss_damage - my_armor
    while True:
        boss_hp_left-=boss_decrease
        if boss_hp_left<=0:
            return(True)
        my_hp_left-=my_decrease
        if my_hp_left <= 0:
            return(False)



for pp in sorted(possible_purchases):
    if not fight(pp):
        print
        print(pp[0],pp)
