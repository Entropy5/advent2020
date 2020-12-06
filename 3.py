import numpy as np
import re

with open("input3.txt") as file:
    lines = file.readlines()
    matrix = []
    for line in lines:
        line = str.strip(line) * 1000
        matrix.append(line)

print(matrix)
line = 0
x = 0
trees = 0
while line < len(matrix):
    line += 2
    x += 1
    if matrix[line][x] == "#":
        trees += 1
    print(trees)
