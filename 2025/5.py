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

# for 
