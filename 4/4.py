#!/usr/bin/env python
from collections import defaultdict
from pprint import pprint
import hashlib

#for i in range(1000000):
for i in range(999609044):
  if (hashlib.md5(('bgvyzdsv'+str(i)).encode('ascii'),usedforsecurity=False).hexdigest())[:5] == '00000':
    print(hashlib.md5(('bgvyzdsv'+str(i)).encode('ascii'),usedforsecurity=False).hexdigest())
    print(i)


