# https://www.hackerrank.com/challenges/jumping-on-the-clouds


import sys


n = int(input().strip())
c = [int(c_temp) for c_temp in input().strip().split(' ')]

current_cloud = 0
jumps = 0

while current_cloud < n - 1:
    if current_cloud == n - 2:
        jumps += 1  # jump to last cloud
        current_cloud += 1
    elif c[current_cloud + 1] == 1:
        jumps += 1
        current_cloud += 2  # jump over immediate thunder
    elif c[current_cloud + 2] == 1:
        jumps += 1
        current_cloud += 1  # set up for thundercloud jump
    else:
        jumps += 1
        current_cloud += 2  # jump far if possible

print(jumps)
