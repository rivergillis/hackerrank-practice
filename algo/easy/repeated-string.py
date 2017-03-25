# https://www.hackerrank.com/challenges/repeated-string

import sys
# works, very fast


s = input().strip()
n = int(input().strip())

num_a = s.count('a')
length = len(s)
total = 0

full_repeats = n // length
extra_chars = n % length
extra_str = s[:extra_chars]

total += full_repeats * num_a
total += extra_str.count('a')

print(total)
