# https://www.hackerrank.com/challenges/between-two-sets

import sys

n, m = input().strip().split(' ')
n, m = [int(n), int(m)]
a = [int(a_temp) for a_temp in input().strip().split(' ')]
b = [int(b_temp) for b_temp in input().strip().split(' ')]

b_factors = list()
betweens = list()
# get all the factors of b
for i in range(1, min(b) + 1):
    can_append = True
    for b_term in b:
        if (b_term % i != 0):
            can_append = False
    if can_append:
        b_factors.append(i)

# keep any numbers n for which every a factors
for factor in b_factors:
    can_append = True
    for a_term in a:
        if (factor % a_term != 0):
            can_append = False
    if can_append:
        betweens.append(factor)
print(len(betweens))
