#!/usr/bin/env python3

from collections import defaultdict, deque
from pprint import pprint

f = "in/11.txt"
# f = "in/11.test.txt"

g = defaultdict(list)

for line in open(f).readlines():
    v, rest = line.strip().split(": ")
    for vv in rest.split(" "):
        g[v].append(vv)

pprint(g)


def dfs(g, start, end, debug=False):
    qq = deque([[start]])
    res = set()
    while len(qq):
        q = qq.popleft()
        v = q[-1]

        for n in g[v]:
            dq = q.copy()
            dq.append(n)

            if n == end:
                if debug:
                    pprint(dq)
                res.add(tuple(dq))
            else:
                qq.appendleft(dq)
    return res


print("first:", len(dfs(g, "you", "out")))

rev = defaultdict(list)
for k, vv in g.items():
    for v in vv:
        rev[v].append(k)


f = dfs(rev, "fft", "svr")
print("first part done", len(f))
o = dfs(g, "dac", "out")
print("third part done", len(o))

d = dfs(g, "fft", "dac")
print("second part done")


# print("second:", len(f) * len(d) * len(o))


# # 3806 is too low
