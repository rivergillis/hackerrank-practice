# https://www.hackerrank.com/challenges/beautiful-triplets

import itertools
import bisect

n, d = input().strip().split(' ')
n, d = [int(n), int(d)]
a = [int(x) for x in input().strip().split(' ')]


def index(a, x):
    i = bisect.bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    return -1

total = 0
for i in range(len(a)):
    a_j = d + a[i]
    j = index(a, a_j)
    if j > i:
        a_k = d + a[j]
        if index(a, a_k) > j:
            total += 1

print(total)
