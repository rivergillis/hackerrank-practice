# https://www.hackerrank.com/challenges/picking-numbers

import sys

n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]

# strategy: make a list for each number in a
matches = dict()

for number in a:
    matches[number] = [x for x in a if (x == number) or (x == (number + 1))]

print(len(max(matches.values(), key=len)))
