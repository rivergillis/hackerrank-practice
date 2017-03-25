# https://www.hackerrank.com/challenges/kangaroo

import sys


x1, v1, x2, v2 = input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]

sys.setrecursionlimit(2500)  # this is bad


def kangaroo(x1, v1, x2, v2):
    if (x1 == x2):
        return True
    elif (x2 > x1 and v2 >= v1):
        return False
    elif (x1 > x2 and v1 >= v2):
        return False
    else:
        return kangaroo(x1 + v1, v1, x2 + v2, v2)

if (kangaroo(x1, v1, x2, v2)):
    print("YES")
else:
    print("NO")
