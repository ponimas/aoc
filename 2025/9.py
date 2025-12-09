#!/usr/bin/env python3
from itertools import islice
from heapq import heappush_max as push, heappop_max as pop
from collections import defaultdict

f = "in/9.txt"
f = "in/9.test.txt"

data = [[int(x) for x in line.split(",")] for line in open(f).readlines()]

areas = []
for i, [x, y] in enumerate(data):
    for j, [dx, dy] in enumerate(islice(data, i + 1), i + 1):
        h = abs(x - dx) + 1
        v = abs(y - dy) + 1
        push(areas, (h * v, [x, y], [dx, dy]))

print("first", pop(areas))

data.sort(key=lambda x: x[1])
filled = set()

by_x = defaultdict(list)
by_y = defaultdict(list)

for x, y in data:
    by_x[x].append((x, y))
    by_y[y].append((x, y))

# for y in range(max_y):
#     l = ["." for _ in range(max_x + 1)]
#     for x, _ in by_y[y]:
#         l[x] = "#"
#     print("".join(l))
