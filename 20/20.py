#!/usr/bin/env python
from collections import defaultdict
from functools import partial, reduce
from itertools import permutations

def get_divisors_sum(n):
    """
    :param n: positive integer.
    :return: list of all different divisors of n.
    """
    if n <= 0:
        return 0
    divisors = [1, n]
    for div in range(1, int(n ** 0.5 + 1)):
        if n % div == 0:
            divisors.extend([n // div, div])
    return sum([x*11 for x in set(divisors) if n // x <=50] )

n=1
while True:
    if n%2048==0:
        print(n)
    if get_divisors_sum(n) > 33100000:
        print(n)
        exit()
    n+=1
