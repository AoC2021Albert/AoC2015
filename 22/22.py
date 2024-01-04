#!/usr/bin/env python
from collections import defaultdict, deque
from functools import partial, reduce
from itertools import permutations
from pprint import pprint
import re
#(cost, damage,heal,(duration,armor,damage,mana))
cost,damage,heal,effect = 0,1,2,3
eduration,earmor,edamage,emana = 0,1,2,3

items=(( 53, 4,0,[0,0,0,0]),
       ( 73, 2,2,[0,0,0,0]),
       (113, 0,0,[6,7,0,0]),
       (173, 0,0,[6,0,3,0]),
       (229, 0,0,[5,0,0,101]))

MY_HP = 50
MY_MANA = 500
BOSS_HP = 58
BOSS_DAMAGE = 9

def test_strategy(play_items):
#    pprint(play_items)
#    if len(play_items)>4:
#        ...
    my_hp=MY_HP
    my_mana=MY_MANA
    boss_hp=BOSS_HP
    boss_damage=BOSS_DAMAGE
    my_effects = []
    round=0
    while True:
        # my turn
        my_armor = 0
        # Effects
        for my_effect in my_effects:
            my_armor+=my_effect[earmor]
            boss_hp-=my_effect[edamage]
            if boss_hp <= 0:
                return(True, True)
            my_mana += my_effect[emana]
            my_effect[eduration]-=1
        # Attack
        if round>=len(play_items):
            # Can't continue, but so far valid
            return(False, True)
        played_item = items[play_items[round]]
        if played_item[cost] > my_mana:
            # Can't play this, ran out of mana
            return(False, False)
        my_mana -= played_item[cost]
        boss_hp -= played_item[damage]
        if boss_hp <=0:
            return(True,True)
        my_hp += played_item[heal]
        my_effects=[me for me in my_effects if me[eduration]>0]
        if played_item[effect][0]!=0:
            # verify I can add the effect
            for ef in my_effects:
                if all(ef[i]==played_item[effect][i] for i in range(1,4)):
                    return(False, False)
            my_effects.append(played_item[effect][:])
        # Boss turn
        my_hp = my_hp - boss_damage + my_armor
        if my_hp <=0:
            return(False, False)
        round+=1



scost, splay_items = 0, 1
strategies = [(0, [])]
#(spent, effects, my_hp, )
cnt=0
while strategies:
    strategies.sort(reverse=True)
    strategy= strategies.pop()
    strategies=strategies[:8000]
    cnt+=1
    if cnt%1000==0:
        print(cnt)
        pprint(strategy)
    wins, valid = test_strategy(strategy[splay_items])
    if wins:
        print(strategy)
        exit()
    if valid:
        spent, plays = strategy
        for i, next_item in enumerate(items):
            strategies.append((spent+next_item[cost], plays+[i]))
