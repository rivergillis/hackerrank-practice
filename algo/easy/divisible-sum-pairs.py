# https://www.hackerrank.com/challenges/divisible-sum-pairs

import sys

n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
a = [int(a_temp) for a_temp in input().strip().split(' ')]

divisibles = list()

for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if ((a[i] + a[j]) % k == 0):
            divisibles.append(tuple([i, j]))

print(len(divisibles))
