# https://www.hackerrank.com/challenges/sock-merchant

import sys


n = int(input().strip())
c = [int(c_temp) for c_temp in input().strip().split(' ')]

num_pairs = 0

distinct = set(c)

for distinct_color in distinct:
    count = c.count(distinct_color)
    while (count >= 2):
        num_pairs += 1
        count -= 2

print(num_pairs)
