# https://www.hackerrank.com/challenges/drawing-book

import sys


n = int(input().strip())
p = int(input().strip())


def turnsfrom1(p):
    return int(p / 2)


def turnsfromn(n, p):
    return int((n - p) / 2)

print(min([turnsfrom1(p), turnsfromn(n, p)]))
