import numpy as np
import re

data = open('input7.txt', 'r').read().split('\n')
d = {}  # bag -> bags that contain it
b = {}  # bag -> bags that it contains
for l in data:
    r = re.search(r"([a-z]* [a-z]*) bags contain (.*).", l)
    if r is not None:
        outer = str.strip(r.group(1))
        content = [(cont.split(sep=" ")) for cont in r.group(2).split(sep=", ")]
        L = []
        for i in range(len(content)):
            if content[i][0] == "no":
                continue
            for j in range(int(content[i][0])):
                name = str.strip(content[i][1] + " " + content[i][2])
                L.append(name)
                if name in d.keys():
                    if outer not in d[name]:
                        d[name].append(outer)
                else:
                    d[name] = [outer]
        b[outer] = L

print(d)
print(b)
answ = []


def look(inner, level):
    if level < 0:
        return
    for outer in d[inner]:
        if outer not in answ:
            answ.append(outer)
        if outer in d.keys():
            look(outer, level - 1)
    return


look("shiny gold", 25)

print(answ)
print(set(answ))
print(len(set(answ)))

answ2 = 0


def look2(outer, level):
    global answ2
    if level < 0:
        return
    for inner in b[outer]:
        answ2 += 1
        if inner in b.keys():
            look2(inner, level - 1)
    return


look2("shiny gold", 50)
print(answ2)
