#!/usr/bin/env python3
import re
from collections import deque

f = "in/10.txt"
# f = 'in/10.test.txt'

rx = re.compile(r"\(([\d,]+)")

data = []


def push(diagram, wiring):
    d = diagram.copy()
    for w in wiring:
        if d[w] == ".":
            d[w] = "#"
        else:
            d[w] = "."
    return d


def find(diagram, wirings):
    ll = len(wirings)
    d = deque((["." for _ in diagram], i, 0) for i in range(ll))

    while len(d):
        state, b, path = d.popleft()
        state = push(state, wirings[b])
        # path = path + [b]
        path += 1

        if "".join(state) == diagram:
            print("".join(state), path)
            return path

        for i in range(ll):
            if i != b:
                d.append((state, i, path))


s = 0
for line in open(f).readlines():
    id = line.index("]")
    diagram = line[1:id]

    iv = line.index("{")
    wirings = [[int(x) for x in w.split(",")] for w in rx.findall(line[id + 1 : iv])]
    s += find(diagram, wirings)

print(s)
