import numpy as np

data = [int(x) for x in open('input10.txt').read().strip().split('\n')]

sdata = np.append([0], np.append(np.sort(data), [np.max(data) + 3]))
ones, threes, onesr = 0, 0, 0
oness = []
for i in range(len(sdata) - 1):
    diff = sdata[i+1] - sdata[i]
    if diff == 1:
        ones += 1
        onesr += 1
    elif diff == 3:
        threes += 1
        oness.append(onesr)
        onesr = 0

print(ones * threes)


def numvalidseq(ons):
    if ons == 1:
        return 1
    if ons == 2:
        return 2
    if ons == 3:
        return 4
    if ons == 4:
        return 7


tot = 1
for i in oness:
    if i != 0:
        tot *= numvalidseq(i)

print(tot)

