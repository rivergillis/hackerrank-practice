# https://www.hackerrank.com/challenges/grading
import sys


def findClosestMultiple(n):
    # returns the closest multiple of 5 to n
    if (n % 5 == 0):
        return n
    else:
        return findClosestMultiple(n + 1)


n = int(input().strip())
for a0 in range(n):
    grade = int(input().strip())
    if (grade < 38):
        print(grade)
    elif (abs(grade - findClosestMultiple(grade)) < 3):
        print(findClosestMultiple(grade))
    else:
        print(grade)
