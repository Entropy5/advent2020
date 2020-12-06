import numpy as np
import re

with open("input2.txt") as file:
    lines = file.readlines()
    correct = 0
    for line in lines:
        extr = re.search(r'(\d*)-(\d*) (\D): (\D*)', line)
        low, high, char, stri = extr.groups()
        # num = len(re.findall(char, stri))
        # if int(low) <= num <= int(high):
        #     correct += 1
        #     print(line, num)
        if (stri[int(low) - 1] == char) != (stri[int(high) - 1] == char):
            correct += 1
    print(correct)
