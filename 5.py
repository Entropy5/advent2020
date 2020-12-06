import numpy as np
import re

with open("input5.txt") as file:
    lines = file.readlines()
    matrix = []
    for line in lines:
        line = str.strip(line)
        matrix.append(line)

ids = []
for line in matrix:
    id = ""
    for let in line:
        if let == "B" or let == "R":
            id += "1"
        else:
            id += "0"
    ids.append(int(id, 2))
print(ids)
print(max(ids))

for i in range(1024):
    if i not in ids:
        print(i)