import sys
import numpy as np
import re

data = [int(x) for x in open('input9.txt').read().strip().split('\n')]

i = 25
ok = True
res = 0

while ok:
    pre = data[i - 25:i]
    res = data[i]
    ook = False
    for a in pre:
        if res - a in pre and res - a != a:
            ook = True
    if not ook:
        print("hit", i, res)
        ok = False
    i += 1

for a in range(len(data[0:502])):
    for b in range(len(data[0:502])):
        if a < b and np.sum(data[a:b]) == res:
            print(np.min(data[a:b]) + np.max(data[a:b]))
