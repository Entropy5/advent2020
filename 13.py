import numpy as np

data = [x for x in open('input13.txt').read().strip().split('\n')]
time = int(data[0])
ids = [x for x in data[1].split(",")]
# ids = ["17", "x", "13", "19"]
# ids = ["67", "7", "x", "59", "61"]
# ids = ["1789", "37", "47", "1889"]
print(ids)

high = 5000
idx = 0
for idi in ids:
    if idi != "x":
        idi = int(idi)
        first = (int(time / idi) + 1) * idi - time
        if first < high:
            high = first
            idx = idi

print("p1", high, idx, high * idx)

# i = 0
# wrong = True
# time_ = -1
# while wrong:
#     i += 1
#     time_ = i * int(ids[0])
#     wrong = False
#     for ii in range(1, len(ids)):
#         if ids[ii] != "x":
#             idi = int(ids[ii])
#             if (int(time_ / idi) + 1) * idi - time_ != ii:
#                 wrong = True
# print("p2", time_)

# CRT stelsel t ~= index modulo id
# t % id == -index

cs = []
ps = []

for i in range(len(ids)):
    if ids[i] != 'x':
        cs.append(-i)
        ps.append(int(ids[i]))
print("cs and ps", cs, ps)


def invert(q, p):
    # inverse of q mod p
    remainder = 1
    a, b = max(p, q), min(p, q)
    q = []
    while remainder != 0:
        q.append(a // b)
        remainder = a - (a // b) * b
        a = b
        b = remainder
    ca = 1
    cb = -q[-2]
    for i in range(-3, -len(q) - 1, -1):
        ca, cb = cb, ca - cb * q[i]
    return ca, cb


def main():
    p = ps  # bus numbers
    c = cs  # eq 0, -19
    res = 0
    for i in range(len(p)):
        p_i = p[i]
        q_i = 1
        for j in range(len(p)):
            if j != i:
                q_i *= p[j]
        nq, np = invert(q_i, p_i)
        res += nq * q_i * c[i]
    return res


res = main()
pp = 1
for pi in ps:
    pp *= pi
while res < 0:
    res += pp
while res > pp:
    res -= pp
print("crt", res)
