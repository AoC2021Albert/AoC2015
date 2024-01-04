#!/usr/bin/env python
from collections import defaultdict
from functools import partial
from itertools import permutations
from pprint import pprint
import json

f = open("12/in.raw", "r")
#f = open("12/sample.raw", "r")

j=json.load(f)

def get_num_value(j):
    if isinstance(j, int):
        return(j)
    if isinstance(j, str):
        return(0)
    if isinstance(j, list):
        return(sum(map(get_num_value,j)))
    if isinstance(j, dict):
        if 'red' in j.values():
            return(0)
        else:
            return(sum(map(get_num_value,j.values())))
    raise Exception('unknown type for {j}')


print(get_num_value(j))