# https://www.hackerrank.com/challenges/migratory-birds

import sys

n = int(input().strip())
types = list(map(int, input().strip().split(' ')))

most_common = types[0]
num_most = 1

type_counts = [0, 0, 0, 0, 0]
type_counts[types[0] - 1] = 1

for i in range(1, len(types)):
    type_counts[types[i] - 1] += 1

for i in range(len(type_counts)):
    if type_counts[i] > num_most:
        print(type_counts[i], " is greater than ", most_common)
        most_common = i + 1
        num_most = type_counts[i]

print(most_common)
print(num_most)
print(type_counts)
