#!/usr/bin/env python3
from bisect import bisect_left

f = "in/5.txt"
# f = "in/5.test.txt"

r, i = open(f).read().strip().split("\n\n")
r = [tuple(map(int, x.split("-")))
     for x in r.split("\n")]
i = [int(x) for x in i.split("\n")]

r.sort()

c = 0
for ii in i:
    for l, j in r:
        if l > ii:
            break
        if l <= ii <= j:
            c += 1
            break
print(c)

merged = set()
n = []

for i, (x, y) in enumerate(r):
    if i in merged:
        continue

    for j in range(i+1, len(r)):
        if y >= r[j][0]:
            y = max(y, r[j][1])
            # print(r[i], r[j])
            merged.add(j)
        else:
            break
    n.append((x, y))

cc = 0
for x, y in n:
    cc += y - x + 1
print(cc)
