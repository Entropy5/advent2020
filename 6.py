import numpy as np
import re

data = open('input6.txt', 'r').read().split('\n\n')
merged = ''.join(line for line in data)
scor1, scor2, sc = 0, 0, 0
for gr in data:
    entr = str.strip(gr).split("\n")
    cat = ''.join(entr)
    grset = ''.join(set(cat))
    scor1 += len(grset)
    for cha in entr[0]:
        if all(cha in x for x in entr):
            sc += 1
    scor2 += sc
    sc = 0

print(scor1)
print(scor2)
