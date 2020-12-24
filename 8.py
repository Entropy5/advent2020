import sys
import numpy as np
import re

dat = open('input8.txt', 'r').read().split('\n')
norm_exit = False
mut_index = 0

while norm_exit is False and mut_index < len(dat):
    ind = 0
    acc = 0
    ran = [False for _ in dat]
    data = dat.copy()
    data[mut_index] = str.replace(data[mut_index], "jmp", "nop")
    while not ran[ind]:
        com = data[ind]
        if com[0:3] == "nop":
            ran[ind] = True
            ind += 1
        if com[0:3] == "acc":
            acc += int(com[4::])
            ran[ind] = True
            ind += 1
        if com[0:3] == "jmp":
            ran[ind] = True
            ind += int(com[4::])
        if ind == len(data) - 1:
            norm_exit = True
            print(ind, acc)
            print("normal stop")
            sys.exit()
    mut_index += 1
