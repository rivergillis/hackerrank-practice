# https://www.hackerrank.com/challenges/cut-the-sticks

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

while arr:
    print(len(arr))
    cut_length = min(arr)
    new_arr = [x - cut_length for x in arr if x - cut_length > 0]

    arr = new_arr
