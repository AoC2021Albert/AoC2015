#!/usr/bin/env python
from collections import defaultdict
from functools import partial
from itertools import permutations
from pprint import pprint

s = "1113222113"
for _ in range(50):
    #print(s)
    ns=""
    pc=" "
    cnt=0
    for i, c in enumerate(s):
        if c!=pc:
            if cnt!=0:
                ns+=str(cnt)+str(pc)
            pc=c
            cnt=1
        else:
            cnt+=1
    ns+=str(cnt)+str(pc)
    s=ns
print(len(s))