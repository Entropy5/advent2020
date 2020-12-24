import math

data = [x for x in open('input12.txt').read().strip().split('\n')]
print(data)


def rotate(x, y, theta):  # rotate x,y around xo,yo by theta (rad)
    theta = math.radians(theta)
    xr = math.cos(theta) * x - math.sin(theta) * y
    yr = math.sin(theta) * x + math.cos(theta) * y
    return [int(round(xr)), int(round(yr))]


E = 0
N = 0
WE = 10
WN = 1

for d in data:
    print("\n", d)
    fir = d[0]
    sec = int(d[1::])
    if fir == "N":
        WN += sec
    elif fir == "S":
        WN -= sec
    elif fir == "E":
        WE += sec
    elif fir == "W":
        WE -= sec
    elif fir == "L":
        new = rotate(WE, WN, sec)
        WE, WN = new[0], new[1]
    elif fir == "R":
        new = rotate(WE, WN, -sec)
        WE, WN = new[0], new[1]
    elif fir == "F":
        E += sec * WE
        N += sec * WN
    else:
        print("????")
    print("c", E, N)
    print("w", WE, WN)

print(abs(N) + abs(E))
