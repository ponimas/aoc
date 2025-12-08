#!/usr/bin/env python3

from functools import reduce
from itertools import islice
from math import sqrt, pow
from heapq import heappush, heappop
from collections import Counter
from operator import mul

wires, f = 1000, "in/8.txt"
# wires, f = 10, 'in/8.test.txt'

data = [[int(x) for x in line.strip().split(",")] for line in open(f).readlines()]

dd = []

for i, x in enumerate(data):
    for j, y in enumerate(islice(data, i + 1, None), i + 1):
        d = sqrt(pow(x[0] - y[0], 2) + pow(x[1] - y[1], 2) + pow(x[2] - y[2], 2))
        heappush(dd, (d, (i, j)))

distances = dd.copy()

clusters = list(range(len(data)))
for _ in range(wires):
    _, (i, j) = heappop(distances)
    ci, cj = sorted([clusters[i], clusters[j]])

    if ci == cj:
        continue

    for k in range(len(data)):
        if clusters[k] == cj:
            clusters[k] = ci


c = dict(Counter(clusters))
m = reduce(mul, sorted(c.values(), reverse=True)[:3])
print("first", m)


distances = dd.copy()
clusters = list(range(len(data)))
li, lj = 0, 0

while len(distances) != 0:
    _, (i, j) = heappop(distances)
    ci, cj = sorted([clusters[i], clusters[j]])

    if ci == cj:
        continue

    li, lj = i, j
    for k in range(len(data)):
        if clusters[k] == cj:
            clusters[k] = ci

print("second", data[li][0] * data[lj][0])
