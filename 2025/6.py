#!/usr/bin/env python3

import sys
from functools import reduce
import operator

f = "in/6.txt"
# f = "in/6.test.txt"

data = [l.split() for l in open(f).read().strip().split("\n")]

def rotate(m):
    return zip(*m[::-1])

s = 0
for l in rotate(data):
    o, *nn = l
    op = operator.mul if o == "*" else operator.add
    s += reduce(op,map(int, nn))

print("first", s)

m = []
for l in rotate(data):
    mm = 0
    for x in l:
        mm = max(mm, len(x))
    m.append(mm)

data = []
for l in open(f).read().strip().split("\n"):
    ll = []
    i = 0
    for mm in m:
        ll.append(l[i:i+mm])
        i += mm
        i += 1
    data.append(ll)

s = 0
for l in rotate(data):
    o, *nn = l
    op = operator.mul if o.strip() == "*" else operator.add
    nn = [int("".join(x).strip() or "0") for x in rotate(nn)]
    s += reduce(op,map(int, nn))

print("second", s)
        
   
