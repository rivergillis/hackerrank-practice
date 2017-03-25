# https://www.hackerrank.com/challenges/jumping-on-the-clouds-revisited

import sys


n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
c = [int(c_temp) for c_temp in input().strip().split(' ')]

current_cloud = 0
current_energy = 100

# initial jump:
current_cloud += k

while current_cloud >= len(c):
    current_cloud -= len(c)

if c[current_cloud] == 1:
    current_energy -= 2
current_energy -= 1

while current_cloud != 0:
    current_cloud += k
    while current_cloud >= len(c):  # overjump
        current_cloud -= len(c)

    if c[current_cloud] == 1:
        current_energy -= 2
    current_energy -= 1

print(current_energy)
