#!/usr/bin/env python3

f = "in/4.test.txt"
f = "in/4.txt"

data = [list(x) for x in open(f).read().strip().split("\n")]

xx = len(data[0]) - 1
yy = len(data) - 1


def n(y, x):
    for dx in [x - 1, x, x + 1]:
        for dy in [y - 1, y, y + 1]:
            if 0 <= dx <= xx and 0 <= dy <= yy and (dx != x or dy != y):
                yield (dy, dx)


c = 0
for y, l in enumerate(data):
    for x, s in enumerate(l):
        if data[y][x] != "@":
            continue
        ns = [(dx, dy) for [dy, dx] in n(y, x) if data[dy][dx] == "@"]
        # print(x, y, ns)
        if len(ns) < 4:
            c += 1

print(c)

cc = 0
while True:
    r = []
    for y, l in enumerate(data):
        for x, s in enumerate(l):
            if data[y][x] != "@":
                continue
            ns = [(dx, dy) for [dy, dx] in n(y, x) if data[dy][dx] == "@"]
            # print(x, y, ns)
            if len(ns) < 4:
                r.append((y, x))
    if len(r) == 0:
        break

    cc += len(r)
    for [y, x] in r:
        data[y][x] = "."

print(cc)
