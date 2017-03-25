# https://www.hackerrank.com/challenges/the-hurdle-race

import sys


n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
height = list(map(int, input().strip().split(' ')))

height_needed = max(height) - k

if (height_needed < 0):
    height_needed = 0
print(height_needed)
