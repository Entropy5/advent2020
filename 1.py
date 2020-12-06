import numpy as np

with open("input1.txt") as file:
    lines = file.readlines()
    numbers = [int(line) for line in lines]

for i in numbers:
    for j in numbers:
        for k in numbers:
            if i + j + k == 2020:
                print(i, j, k, i * j * k)

