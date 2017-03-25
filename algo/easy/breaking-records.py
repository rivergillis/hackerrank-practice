# https://www.hackerrank.com/challenges/breaking-best-and-worst-records

import sys


n = int(input().strip())
score = list(map(int, input().strip().split(' ')))

best = worst = score[0]
num_best = 0
num_worst = 0

for s in score:
    if s > best:
        num_best += 1
        best = s
    elif s < worst:
        num_worst += 1
        worst = s

print(num_best, num_worst)
