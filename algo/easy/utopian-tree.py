# https://www.hackerrank.com/challenges/utopian-tree

import sys


def utopian(n, i, h):
    # n: number of intervals, constant
    # i: current interval, subs by 1
    # h: current height, grows
    #print("in utopain with n=", n, "i=", i, "h=", h)
    if n == i:
        return h

    if i % 2 == 1:
        return utopian(n, i + 1, h + 1)
    else:
        return utopian(n, i + 1, h * 2)

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(utopian(n, 0, 1))
