#!/usr/bin/env python3


f = "in/7.txt"
# f = 'in/7.test.txt'

data = open(f).read().strip().splitlines()

s = data[0].index("S")
timelines = [0] * len(data[0])
timelines[s] = 1
cnt = 0

for l in data[1:]:
    if "^" not in l:
        continue

    n = [0] * len(l)

    for i, x in enumerate(timelines):
        if x == 0:
            continue
        if l[i] == "^":
            cnt += 1
            n[i - 1] += x
            n[i + 1] += x
        else:
            n[i] += x
    timelines = n


print(cnt)
print(sum(timelines))
