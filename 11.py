data = [x for x in open('input11.txt').read().strip().split('\n')]
cols, rows = len(data[0]), len(data)
for ri in range(rows):
    data[ri] = '.' + data[ri] + '.'
data = ['.' * (cols + 2)] + data + ['.' * (cols + 2)]
print(data)


def loop(data):
    ndata = data.copy()
    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            nocc = 0
            M = [-1, -1, -1, 0, 0, 1, 1, 1]
            N = [-1, 0, 1, -1, 1, -1, 0, 1]
            for k in range(8):
                looking = True
                rang = 1
                while looking:
                    if i + rang * M[k] < 1 or i + rang * M[k] > rows + 1 or j + rang * N[k] < 1 or j + rang * N[k] > cols + 1:
                        break
                    if data[i + rang * M[k]][j + rang * N[k]] == "#":
                        looking = False
                        nocc += 1
                    elif data[i + rang * M[k]][j + rang * N[k]] == "L":
                        looking = False
                    else:
                        rang += 1
            if data[i][j] == "L" and nocc == 0:
                new = list(ndata[i])
                new[j] = '#'
                ndata[i] = ''.join(new)
            elif data[i][j] == "#" and nocc >= 5:
                new = list(ndata[i])
                new[j] = 'L'
                ndata[i] = ''.join(new)
    return ndata


for i in range(1000):
    data = loop(data)
    count = 0
    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            if data[i][j] == "#":
                count += 1
    print("c", count)
