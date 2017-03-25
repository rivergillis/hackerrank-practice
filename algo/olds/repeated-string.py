# https://www.hackerrank.com/challenges/repeated-string

import sys
# works, too slow


def getnext(s, n):
    i = 0
    while n:
        #print("in gn, i=", i)
        if i == len(s):
            i = 0
        yield s[i]
        i += 1
        n -= 1

s = input().strip()
n = int(input().strip())

num_a = s.count('a')
length = len(s)

#total = num_a * (n // len(s))
total = 0
for ch in getnext(s, n):
    if ch == 'a':
        total += 1

print(total)
